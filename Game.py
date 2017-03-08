
# coding: utf-8
from HealthTableau import HealthTableau
import HealthPoints
from obsub import event

class Game(object):
    def __init__(self) -> None:
        self.log_lines = []
        self.hta = self.make_health_tableau()
        self.htb = self.make_health_tableau()
    def make_health_tableau(self) -> HealthTableau:
        ht = HealthTableau()
        ht.insert_point('Heart')
        ht.insert_point('Splanch')
        ht.insert_point('Phylactery')
        ht.insert_point('Arm')
        ht.insert_point('Arm')
        return ht
    def advance(self) -> None:
        if not self.hta.is_dead():
            self.hta.defend(self.hta._abilities, self.htb)
            self.log("Damaged. {0}.".format("Dead" if self.hta.is_dead() else "Not dead"))
    def log(self, text : str) -> None:
        self.log_lines.append(text)
        self.on_log()
    @event
    def on_log(self): pass
