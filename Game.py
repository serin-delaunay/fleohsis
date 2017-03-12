
# coding: utf-8
from AbilityBag import AbilityBag
from HealthTableau import HealthTableau
from HealthPoint import HealthPoint
from typing import Optional
from obsub import event
from random import choice
from Logger import messages, debug

class Game(object):
    def __init__(self) -> None:
        self.hta = self.make_generic_health_tableau()
        self.htb = self.make_generic_health_tableau()
        self.turn_a = True
    def make_generic_health_tableau(self) -> HealthTableau:
        ht = HealthTableau()
        ht.insert_point('Heart')
        ht.insert_point('Splanch')
        ht.insert_point('Phylactery')
        ht.insert_point('Arm')
        ht.insert_point('SpareMuscles')
        ht.insert_point('Spear')
        return ht
    def process_attack(self,
                       defender : HealthTableau,
                       attacker : Optional[HealthTableau]=None,
                       weapon : Optional[HealthPoint]=None,
                       attack_mode : Optional[str]=None) -> None:
        event_args = {
            'attacker':attacker,
            'defender':defender,
            'weapon':weapon,
            'attack_mode':attack_mode
        }
        debug.log('preparing attack')
        weapon.get_abilities().call('prepare_attack', event_args)
        debug.log('augmenting attack')
        attacker.call('augment_attack', event_args)
        damage_tableau = event_args['damage_tableau']
        debug.log('executing attack')
        damage_tableau.execute_attack(event_args)
    def advance(self) -> None:
        if self.turn_a:
            attacker = self.hta
            defender = self.htb
        else:
            attacker = self.htb
            defender = self.hta
        self.turn_a = not self.turn_a
        if attacker.is_dead():
            messages.log('Too dead to attack')
        elif defender.is_dead():
            messages.log('No point attacking a corpse')
        else:
            event_args = {
                'attacker':attacker,
                'attack_modes':[]
            }
            for health_point in attacker:
                event_args['weapon'] = health_point
                health_point.get_abilities().call('list_attack_modes', event_args)
            attack_modes = event_args['attack_modes']
            if attack_modes:
                debug.log('possible attack modes: {0}'.format(attack_modes))
                weapon, attack_mode = choice(attack_modes)
                debug.log('chosen attack mode: {0}, {1}'.format(weapon, attack_mode))
                self.process_attack(defender, attacker, weapon, attack_mode)
                messages.log("Damaged. {0}.".format(
                    "Dead" if defender.is_dead() else "Not dead"))
            else:
                    messages.log("Unable to attack")
