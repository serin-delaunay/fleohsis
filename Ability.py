
# coding: utf-8
from typing import Dict
from AbilityHooks import get_hook

_abilities = {}

class Ability(object):
    def __init__(self, name : str, description : str, hidden : bool = False,
                 **kwargs : Dict[str,str]) -> None:
        self.name = name
        self.description = description
        self.hidden = hidden
        self.hooks = {k: get_hook(v) for k,v in kwargs.items()}
        assert(self.name not in _abilities)
        _abilities[self.name] = self
    def __repr__(self) -> str:
        return "Ability: {0}".format(self.name)
