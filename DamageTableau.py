
# coding: utf-8
from typing import List, Union
from DamagePoint import DamagePoint
from Ability import Ability
from AbilityBag import AbilityBag

class DamageTableau(object):
    def __init__(self,
                 common_abilities : List[Union[str,Ability]],
                 damage_points : List[List[Union[str,Ability]]]):
        self._common_abilities = AbilityBag(common_abilities)
        self._damage_points = [DamagePoint(*point) for point in damage_points]
    def add_common_abilities(self, abilities : List[Union[str,Ability]]):
        self._common_abilities.add_abilities(abilities)
        for point in self._damage_points:
            point.add_abilities(abilities)
    def add_damage_point(self, point : DamagePoint):
        point.add_abilities(self._common_abilities.names())
        self._damage_points.append(point)
    def execute_attack(self, event_args):
        for point in self._damage_points:
            event_args['damage_point'] = point
            point.call('execute_attack', event_args)
