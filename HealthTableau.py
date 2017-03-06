
# coding: utf-8

# In[ ]:

from collections import Counter
from typing import List, Union, Optional


# In[ ]:

from HealthPoint import HealthPoint
from Ability import Ability


# In[ ]:

class HealthTableau(object):
    def __init__(self) -> None:
        self._health_points = []
        self._ability_counter = Counter()
        self._abilities_by_name = {}
    def _add_abilities(self, abilities: List[Ability]) -> None:
        self._ability_counter.update(x.name for x in abilities)
        self._abilities_by_name.update((x.name, x.hooks) for x in abilities)
    def _remove_abilities(self, abilities: List[Ability]) -> None:
        self._ability_counter.subtract(x.name for x in abilities)
    def insert_point(self, health_point: HealthPoint, index : Optional[int] = None) -> None:
        if index is None:
            self._health_points.append(health_point)
        else:
            self._health_points.insert(index, health_point)
        self._add_abilities(health_point.get_abilities())
    def remove_point(self, index: int) -> None:
        del self._health_points[index]
        self._remove_abilities(health_point.get_abilities())
    def damage_point(self, index: int) -> None:
        health_point = self._health_points[index]
        if health_point.is_healthy:
            self._remove_abilities(health_point.get_abilities())
            health_point.is_healthy = False
            self._add_abilities(health_point.get_abilities())
    def inflict_damage(self) -> None:
        # TODO account for different attack and defense abilities
        for i in range(len(self._health_points)-1,-1,-1):
            if(self._health_points[i].is_healthy):
                self.damage_point(i)
                return
    def has_ability(self, ability: Union[str, Ability]) -> bool:
        if type(ability) == Ability:
            return self._ability_counter[ability.name] > 0
        else:
            return self._ability_counter[ability] > 0
    def is_dead(self) -> bool:
        if self.has_ability('Undead'):
            return False
        elif self.has_ability('Dead'):
            return True
        else:
            return not self.has_ability('Alive')
    def __repr__(self) -> str:
        return "HealthTableau{0}".format(tuple(self._health_points))

