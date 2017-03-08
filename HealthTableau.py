
# coding: utf-8
from typing import List, Union, Optional, Iterator, Any, TypeVar
from obsub import event

from HealthPoint import HealthPoint
from HealthPoints import get_health_point
from Ability import Ability
from AbilityBag import AbilityBag

T = TypeVar('T',bound='HealthTableau')
class HealthTableau(object):
    def __init__(self) -> None:
        self._health_points = []
        self._abilities = AbilityBag()
    def __iter__(self) -> Iterator[HealthPoint]:
        return iter(self._health_points)
    def __getitem__(self, index : int) -> HealthPoint:
        return self._health_points[index]
    def __len__(self) -> int:
        return len(self._health_points)
    def before_point_state_change(self, health_point):
        self._abilities.remove_abilities(health_point.get_abilities().names())
    def after_point_state_change(self, health_point):
        self._abilities.add_abilities(health_point.get_abilities().names())
    def insert_point(self, health_point: str, index : Optional[int] = None) -> None:
        health_point = get_health_point(health_point)
        if index is None:
            self._health_points.append(health_point)
        else:
            self._health_points.insert(index, health_point)
        health_point.before_health_change += self.before_point_state_change
        health_point.after_health_change += self.after_point_state_change
        self._abilities.add_abilities(health_point.get_abilities().names())
    def remove_point(self, index: int) -> None:
        health_point = self._health_points[index]
        self._abilities.remove_abilities(health_point.get_abilities().names())
        del self._health_points[index]
    def defend(self : T,
               attack_abilities : AbilityBag,
               attacker : T,
               attack_mode : Optional[str]=None) -> None:
        event_args = {
            'attacker':attacker,
            'attack_abilities':attack_abilities,
            'defender':self,
            'attack_mode':attack_mode
        }
        attack_abilities.call('begin_attack',event_args)
    def is_dead(self) -> bool:
        if self._abilities.has_ability('Undead'):
            return False
        elif self_abilities.has_ability('Dead'):
            return True
        else:
            return not self._abilities.has_ability('Alive')
    def __repr__(self) -> str:
        return "HealthTableau{0}".format(tuple(self._health_points))
    @event
    def on_altered(self): pass


