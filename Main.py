import sys
import time
from typing import List
from json import load

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from MainwindowUi import MainwindowUi
from Particle import Particle
from Simulation import Simulation
from Vector2D import Vector2D
from threading import Thread, Condition


class ListItem(object):
    def __init__(self, particle: Particle):
        self.particle = particle
        self.label = repr(particle)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.simulation_instance = None
        self.ui = MainwindowUi()
        self.ui.setupUi(self)
        self.current_min_free_id: int = 1
        self.particle_list: List[ListItem] = []
        self.draw_condition = Condition()
        self.fps_limit: int = 30
        self.draw_cycle_thread = Thread(target=self.draw_cycle)
        self.simulation_cycle_thread = Thread(target=self.simulation_cycle)
        self.simulation_running = False
        with open("config.json") as f:
            self.config = load(f)

        # CONNECTIONS
        self.ui.btnNew.clicked.connect(self.add_particle)
        self.ui.btnDelete.clicked.connect(self.remove_particle)
        self.ui.btnSimStart.clicked.connect(self.start_simulation)
        self.ui.btnSimStop.clicked.connect(self.stop_simulation)

    def update_list_view(self):
        self.ui.lstBodies.clear()
        self.ui.lstBodies.addItems([x.label for x in self.particle_list])

    def add_particle(self):
        temp = Particle(id=self.current_min_free_id,
                        position=Vector2D(self.ui.spbPosX.value(), self.ui.spbPosY.value()),
                        velocity=Vector2D(self.ui.spbSpdX.value(), self.ui.spbSpdY.value()),
                        mass=self.ui.spbMass.value(),
                        radius=self.ui.spbRadius.value())
        self.particle_list.append(ListItem(temp))
        self.current_min_free_id += 1
        self.update_list_view()

    def remove_particle(self):
        selected_item = self.ui.lstBodies.selectedItems()[0].text()
        for i in range(len(self.particle_list)):
            if self.particle_list[i].label == selected_item:
                self.particle_list.pop(i)
                break
        self.update_list_view()

    def start_simulation(self):
        self.simulation_instance = Simulation(particles=[x.particle for x in self.particle_list],
                                              framesize=(int(self.config["SIMULATION"]["frame_size_x"]),
                                                         int(self.config["SIMULATION"]["frame_size_y"])))
        self.simulation_running = True
        self.simulation_cycle_thread.start()
        self.draw_cycle_thread.start()

    def stop_simulation(self):
        self.simulation_running = False
        self.draw_cycle_thread.join()
        self.simulation_cycle_thread.join()

    def draw_cycle(self):
        while self.simulation_running:
            with self.draw_condition:
                self.draw_condition.notify()
                time.sleep(1 / self.fps_limit)

    def simulation_cycle(self):
        while self.simulation_running:
            with self.draw_condition:
                self.draw_condition.wait()
                self.ui.lblSimulationDisplay.setPixmap(QPixmap.fromImage(self.simulation_instance.run_step(False)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
