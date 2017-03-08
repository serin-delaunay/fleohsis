
# coding: utf-8
from typing import List, TypeVar
from obsub import event
from sortedcontainers import SortedListWithKey
from AbilityBag import AbilityBag
from Abilities import get_ability
from Ability import Ability

T = TypeVar('T', bound='HealthPoint')
class HealthPoint(object):
    def __init__(self, name : str,
                 healthy_abilities : List[str],
                 damaged_abilities : List[str]) -> None:
        self.name = name
        self._healthy_abilities = AbilityBag(healthy_abilities)
        self._damaged_abilities = AbilityBag(damaged_abilities)
        self.description = self.make_description()
        self.__is_healthy = True
    def _get_health(self) -> bool:
        return self.__is_healthy
    def _set_health(self, health) -> None:
        if self.__is_healthy != health:
            self.before_health_change()
            self.__is_healthy = health
            self.after_health_change()
    @event
    def before_health_change(self): pass
    @event
    def after_health_change(self): pass
    
    is_healthy = property(_get_health, _set_health)
    def make_description(self) -> str:
        healthy_description = '\n'.join(x.description
                                        for x in self._healthy_abilities.abilities())
        damaged_description = '\n'.join(x.description
                                        for x in self._damaged_abilities.abilities())
        descriptions = []
        if healthy_description:
            descriptions.append('Healthy:\n' + healthy_description)
        if damaged_description:
            descriptions.append('Damaged:\n' + damaged_description)
        return '\n'.join(descriptions)
    def get_abilities(self) -> AbilityBag:
        if self.is_healthy:
            return self._healthy_abilities
        else:
            return self._damaged_abilities
    def copy(self : T) -> T:
        return HealthPoint(self.name,
                           list(self._healthy_abilities.names()),
                           list(self._damaged_abilities.names()))
    def __repr__(self) -> str:
        return "HealthPoint: {0}({1})".format(self.name,
                                              "healthy" if self.is_healthy
                                              else "damaged")
    def summary(self) -> str:
        return '[color=white]{0}({1}[color=white])'.format(
            self.name,
            "[color=green]healthy" if self.is_healthy
            else "[color=red]damaged")
