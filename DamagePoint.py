
# coding: utf-8
from typing import List, Optional, Union
from Ability import Ability
from HealthPoint import HealthPoint

class DamagePoint(object):
    def __init__(self, abilities : List[str], source : Optional[HealthPoint] = None):
        from AbilityBag import AbilityBag
        self.abilities = AbilityBag(abilities)
        self.source = source
    def add_abilities(self, abilities : List[Union[str,Ability]]):
        self.abilities.add_abilities(abilities)
    def call(self, event, event_args):
        self.abilities.call(event, event_args)
    def copy(self):
        return DamagePoint(self.abilities.names(), self.source)
