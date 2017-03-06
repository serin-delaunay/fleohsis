
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
ColourRGBA.__new__.__defaults__ = (255,)

class ColourName(Colour):
    def __init__(self, name) -> None:
        self.name = name
    def blt_colour(self) -> int:
        return blt.color_from_name(self.name)

class ColourBLT(Colour):
    def __init__(self, code) -> None:
        self.code = code
    def blt_colour(self) -> int:
        return self.code
