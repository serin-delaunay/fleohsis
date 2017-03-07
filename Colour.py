
# coding: utf-8
from bearlibterminal import terminal as blt
from abc import ABCMeta, abstractmethod
from typing import NamedTuple

class Colour(metaclass=ABCMeta):
    @abstractmethod
    def blt_colour(self) -> int : pass

class ColourRGBA(Colour, NamedTuple('RGBA', [('r',int),('g',int),('b',int),('a',int)])):
    def blt_colour(self) -> int:
        return blt.color_from_argb(self.a, self.r, self.g, self.b)
ColourRGBA.__new__.__defaults__ = (255,) # mypy hates this
# When Python 3.6.1 arrives:
#   * Remove __defaults__ assignment
#   * Use class _ColourRGBA(NamedTuple)
#   * Assign defaults in instance variable type hints
#   * Use class ColourRGBA(NamedTuple, Colour), to avoid metaclass conflict

class ColourName(Colour):
    name : str
    def __init__(self, name : str) -> None:
        self.name = name
    def blt_colour(self) -> int:
        return blt.color_from_name(self.name)

class ColourBLT(Colour):
    code : int
    def __init__(self, code : int) -> None:
        self.code = code
    def blt_colour(self) -> int:
        return self.code
