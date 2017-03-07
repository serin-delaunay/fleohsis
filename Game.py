
# coding: utf-8
from HealthTableau import HealthTableau
import HealthPoints
from obsub import event

class Game(object):
    def __init__(self) -> None:
        self.ht = HealthTableau()
        self.ht.insert_point(HealthPoints.Heart.copy())
        self.ht.insert_point(HealthPoints.Splanch.copy())
        self.ht.insert_point(HealthPoints.Phylactery.copy())
        self.ht.insert_point(HealthPoints.Arm.copy())
        self.ht.insert_point(HealthPoints.Arm.copy())
        self.log_lines = []
    def advance(self) -> None:
        if not self.ht.is_dead():
            self.ht.inflict_damage()
            self.log("Damaged. {0}.".format("Dead" if self.ht.is_dead() else "Not dead"))
    def log(self, text : str) -> None:
        self.log_lines.append(text)
        self.on_log()
    @event
    def on_log(self): pass
