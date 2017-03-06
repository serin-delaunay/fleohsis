
# coding: utf-8
from typing import Callable

class Ability(object):
    def __init__(self, name : str, description : str, **kwargs : Callable[..., None]) -> None:
        self.name = name
        self.description = description
        self.hooks = kwargs
    def __repr__(self) -> str:
        return "Ability: {0}".format(self.name)
