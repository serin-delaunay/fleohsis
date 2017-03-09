
# coding: utf-8
from AbilityBag import AbilityBag
from HealthTableau import HealthTableau
import HealthPoints
from typing import Optional
from obsub import event
from Logger import messages, debug

class Game(object):
    def __init__(self) -> None:
        self.hta = self.make_generic_health_tableau()
        self.htb = self.make_generic_health_tableau()
        self.attack_bag = self.make_generic_attack_abilities()
    def make_generic_health_tableau(self) -> HealthTableau:
        ht = HealthTableau()
        ht.insert_point('Heart')
        ht.insert_point('Splanch')
        ht.insert_point('Phylactery')
        ht.insert_point('Arm')
        ht.insert_point('Arm')
        return ht
    def make_generic_attack_abilities(self) -> AbilityBag:
        ab = AbilityBag(['Begin Attack','Target Attack (Normal)'])
        return ab
    def process_attack(self,
                       defender : HealthTableau,
                       attack_abilities : AbilityBag,
                       attacker : Optional[HealthTableau],
                       attack_mode : Optional[str]=None) -> None:
        event_args = {
            'attacker':attacker,
            'attack_abilities':attack_abilities,
            'defender':defender,
            'attack_mode':attack_mode
        }
        debug.log('about to begin attack')
        attack_abilities.call('begin_attack',event_args)
    def advance(self) -> None:
        if not self.hta.is_dead():
            self.process_attack(self.hta, self.attack_bag, self.htb)
            messages.log("Damaged. {0}.".format("Dead" if self.hta.is_dead() else "Not dead"))
