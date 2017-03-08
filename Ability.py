
# coding: utf-8
from typing import Dict
from AbilityHooks import get_ability

class Ability(object):
    def __init__(self, name : str, description : str, **kwargs : Dict[str,str]) -> None:
        self.name = name
        self.description = description
        self.hooks = {k: get_ability(v) for k,v in kwargs.items()}
    def __repr__(self) -> str:
        return "Ability: {0}".format(self.name)
