
# coding: utf-8
from typing import Dict, List, Union

_abilities = {}

class Ability(object):
    def __init__(self, name : str, description : str, hidden : bool = False,
                 **kwargs : Dict[str,Union[str,List[str]]]) -> None:
        from Hooks import get_hook # avoid circular from ... import
        self.name = name
        self.description = description
        self.hidden = hidden
        
        self.hooks = {k: list(map(get_hook, [v] if isinstance(v,str) else v))
                      for k,v in kwargs.items()}
        assert(self.name not in _abilities)
        _abilities[self.name] = self
    def __repr__(self) -> str:
        return "Ability: {0}".format(self.name)
