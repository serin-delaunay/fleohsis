
# coding: utf-8
from typing import List, TypeVar

from Ability import Ability

T = TypeVar('T', bound='HealthPoint')
class HealthPoint(object):
    def __init__(self, name : str,
                 healthy_abilities : List[Ability],
                 damaged_abilities : List[Ability]) -> None:
        self.name = name
        self.healthy_abilities = healthy_abilities
        self.damaged_abilities = damaged_abilities
        self.description = self.make_description()
        self.is_healthy = True
    def make_description(self) -> str:
        healthy_description = '\n'.join(x.description for x in self.healthy_abilities)
        damaged_description = '\n'.join(x.description for x in self.damaged_abilities)
        descriptions = []
        if healthy_description:
            descriptions.append('Healthy:\n' + healthy_description)
        if damaged_description:
            descriptions.append('Damaged:\n' + damaged_description)
        return '\n'.join(descriptions)
    def get_abilities(self) -> List[Ability]:
        if self.is_healthy:
            return self.healthy_abilities
        else:
            return self.damaged_abilities
    def copy(self : T) -> T:
        return HealthPoint(self.name, self.healthy_abilities, self.damaged_abilities)
    def __repr__(self) -> str:
        return "HealthPoint: {0}({1})".format(self.name, "healthy" if self.is_healthy else "damaged")
