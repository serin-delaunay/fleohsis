
# coding: utf-8
from collections import Counter
from typing import List, Union, Optional, Iterator
from obsub import event

from HealthPoint import HealthPoint
from Ability import Ability

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
    def __iter__(self) -> Iterator[HealthPoint]:
        return iter(self._health_points)
    def before_point_state_change(self, health_point):
        self._remove_abilities(health_point.get_abilities())
    def after_point_state_change(self, health_point):
        self._add_abilities(health_point.get_abilities())
    def insert_point(self, health_point: HealthPoint, index : Optional[int] = None) -> None:
        if index is None:
            self._health_points.append(health_point)
        else:
            self._health_points.insert(index, health_point)
        health_point.before_health_change += self.before_point_state_change
        health_point.after_health_change += self.after_point_state_change
        self._add_abilities(health_point.get_abilities())
    def remove_point(self, index: int) -> None:
        health_point = self._health_points[index]
        self._remove_abilities(health_point.get_abilities())
        del health_point
    def inflict_damage(self) -> None:
        # TODO account for different attack and defense abilities
        for health_point in reversed(self._health_points):
            if(health_point.is_healthy):
                health_point.is_healthy = False
                return
    def has_ability(self, ability: Union[str, Ability]) -> bool:
        if isinstance(ability, Ability):
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
    @event
    def on_altered(self): pass
