import sys
import time
from threading import Thread, Condition
from typing import List

import PySide6.QtCore as QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from MainwindowUi import MainwindowUi
from SaveLoad import *
from Simulation import Simulation


class ListItem(object): # Helps to associate captions in the lstBodies to the Particle class objects
    def __init__(self, particle: Particle):
        self.particle = particle
        self.label = repr(particle)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() # Load the interface from MainwindowUi file
        self.simulation_cycle_thread = None
        self.draw_cycle_thread = None
        self.simulation_instance = None
        self.ui = MainwindowUi()
        self.ui.setupUi(self)
        self.current_min_free_id: int = 1 # Minimal unoccupied particle id
        self.particle_list: List[ListItem] = []
        self.draw_condition = Condition()


        self.simulation_running = False
        with open("config.json") as f: # Load the config file
            self.config = load(f)

        self.frame_delay: float = 1 / self.config["SIMULATION"]["fps_limit"] # Set the minimal delay between frames

        # Connect the functions to the corresponding buttons
        self.ui.btnAdd.clicked.connect(self.add_particle)
        self.ui.btnDelete.clicked.connect(self.remove_particle)
        self.ui.btnSimStart.clicked.connect(self.start_simulation)
        self.ui.btnSimStop.clicked.connect(self.stop_simulation)
        self.ui.btnSimStep.clicked.connect(self.run_single_step)
        self.ui.btnShowHeatMap.clicked.connect(self.draw_heatmap)
        self.ui.btnSave.clicked.connect(self.save_state_to_file)
        self.ui.btnLoad.clicked.connect(self.load_state_from_file)
        self.ui.btnEdit.clicked.connect(self.edit_particle)

        # Disable the buttons to prevent exceptions
        self.ui.btnShowHeatMap.setDisabled(True)
        self.ui.btnSimStop.setDisabled(True)
        self.ui.cbbColorDependsOn.setDisabled(True)

    def closeEvent(self, *args, **kwargs): # Ensure that additional threads are stopped whe the app is exited
        super(QMainWindow, self).closeEvent(*args, **kwargs)
        if self.simulation_running:
            self.stop_simulation()

    def update_list_view(self): # Manually update the lstBodies to reflect any changes
        self.ui.lstBodies.clear()
        self.ui.lstBodies.addItems([x.label for x in self.particle_list])

    def add_particle(self):
        temp = Particle(id=self.current_min_free_id,
                        position=Vector2D(self.ui.spbPosX.value(), self.ui.spbPosY.value()),
                        velocity=Vector2D(self.ui.spbSpdX.value(), self.ui.spbSpdY.value()),
                        mass=self.ui.spbMass.value(),
                        radius=self.ui.spbRadius.value())
        self.particle_list.append(ListItem(temp))
        self.current_min_free_id = len(self.particle_list) + 1
        self.update_list_view()

    def remove_particle(self):
        selected_item = self.ui.lstBodies.selectedItems()[0].text()
        for i in range(len(self.particle_list)):
            if self.particle_list[i].label == selected_item:
                self.particle_list.pop(i)
                self.current_min_free_id = i + 1
                break
        self.update_list_view()

    def edit_particle(self): # Replace the selected lstBodies item with another one that has new parameters
        selected_item = self.ui.lstBodies.selectedItems()[0].text()
        for i in range(len(self.particle_list)):
            if self.particle_list[i].label == selected_item:
                self.particle_list[i] = ListItem(particle=Particle(id=i+1,
                                                                   position=Vector2D(self.ui.spbPosX.value(),
                                                                                     self.ui.spbPosY.value()),
                                                                   velocity=Vector2D(self.ui.spbSpdX.value(),
                                                                                     self.ui.spbSpdY.value()),
                                                                   mass=self.ui.spbMass.value(),
                                                                   radius=self.ui.spbRadius.value()))
                break
        self.update_list_view()

    def load_state_from_file(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  caption="Загрузить начальное состояние из файла",
                                                  filter="JSON files (*.json)",
                                                  dir="./saves/")
        new_particles = load_initial_state(filename)
        self.particle_list = [] # Delete all particles
        for particle in new_particles:
            self.particle_list.append(ListItem(particle)) # Load new ones from the savefile
        self.update_list_view()

    def save_state_to_file(self):
        filename, _ = QFileDialog.getSaveFileName(self,
                                                  caption="Сохранить начальное состояние в файл",
                                                  filter="JSON files (*.json)",
                                                  dir="./saves/")
        save_initial_state([x.particle for x in self.particle_list], filename)
    def start_simulation(self):
        self.simulation_instance = Simulation(particles=[x.particle for x in self.particle_list],
                                              framesize=(int(self.config["SIMULATION"]["frame_size_x"]),
                                                         int(self.config["SIMULATION"]["frame_size_y"]))) # Create a new simulation instance
        self.simulation_running = True
        self.draw_cycle_thread = Thread(target=self.draw_cycle)
        self.simulation_cycle_thread = Thread(target=self.simulation_cycle)
        self.simulation_cycle_thread.start() # Start additional threads
        self.draw_cycle_thread.start()
        self.ui.btnShowHeatMap.setDisabled(True) # Disable buttons to prevent exceptions
        self.ui.btnSimStart.setDisabled(True)
        self.ui.btnSimStep.setDisabled(True)
        self.ui.gpbEdit.setDisabled(True)
        self.ui.btnSimStop.setEnabled(True) # Enable the buttons that stops the simulation

    def stop_simulation(self):
        self.simulation_running = False
        self.simulation_cycle_thread.join() # Join the threads
        self.draw_cycle_thread.join()
        self.ui.btnShowHeatMap.setEnabled(True) # Enable buttons
        self.ui.btnSimStart.setEnabled(True)
        self.ui.btnSimStep.setEnabled(True)
        self.ui.gpbEdit.setEnabled(True)
        self.ui.btnSimStop.setDisabled(True)

    def draw_cycle(self):
        while self.simulation_running:
            with self.draw_condition:
                self.draw_condition.notify() # Allow the new step to be rendered
                time.sleep(self.frame_delay) # Wait the minimal delay

    def get_dependent_coloring_type(self) -> str: # Convert the selected text to pre-defined values
        match self.ui.cbbColorDependsOn.currentText():
            case "скорости":
                return "velocity"
            case "ускорения":
                return "acceleration"

    def simulation_cycle(self):
        while self.simulation_running:
            with self.draw_condition:
                self.draw_condition.wait(1.0) # Wait until the permission from draw_cycle, but no more than 1 second
                self.ui.lblSimulationDisplay.setPixmap(QPixmap.fromImage(
                    self.simulation_instance.run_step( # Generate the new frame
                        draw_barycenter=self.ui.cbxDrawMassCenter.isChecked(),
                        draw_velocity_vectors=self.ui.cbxDrawSpdVects.isChecked(),
                        draw_trails=self.ui.cbxDrawTrails.isChecked(),
                        dependent_coloring=self.ui.cbxColorDependent.isChecked(),
                        dependent_coloring_type=self.get_dependent_coloring_type())).scaled(
                    self.ui.lblSimulationDisplay.width(),
                    self.ui.lblSimulationDisplay.height(),
                    QtCore.Qt.KeepAspectRatio # Resize it so it fits the size of lblSimulationDisplay
                ))

    def draw_heatmap(self): # Generate the force heatmap
        self.ui.lblSimulationDisplay.setPixmap(QPixmap.fromImage(
            self.simulation_instance.draw_force_heatmap().scaled(
                self.ui.lblSimulationDisplay.width(),
                self.ui.lblSimulationDisplay.height(),
                QtCore.Qt.KeepAspectRatio
            )))

    def run_single_step(self): # Generates the next frame of current simulation
        self.ui.lblSimulationDisplay.setPixmap(QPixmap.fromImage(
            self.simulation_instance.run_step(
                draw_barycenter=self.ui.cbxDrawMassCenter.isChecked(),
                draw_velocity_vectors=self.ui.cbxDrawSpdVects.isChecked(),
                draw_trails=self.ui.cbxDrawTrails.isChecked(),
                dependent_coloring=self.ui.cbxColorDependent.isChecked(),
                dependent_coloring_type=self.get_dependent_coloring_type())).scaled(
            self.ui.lblSimulationDisplay.width(),
            self.ui.lblSimulationDisplay.height(),
            QtCore.Qt.KeepAspectRatio
        ))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
