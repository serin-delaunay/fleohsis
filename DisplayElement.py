
# coding: utf-8
from typing import NamedTuple, Optional, Union
from bearlibterminal import terminal as blt
from abc import ABCMeta, abstractmethod
from vec import ivec
from Colour import Colour, ColourRGBA

class DisplayElement(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, xy : ivec) -> None: pass

class PutArgs(DisplayElement,
              NamedTuple('PutArgs',
                         [('char', Union[int,str]),
                          ('xy', ivec),
                          ('fg_colour', Colour),
                          ('bg_colour', Optional[Colour])
                         ])):
    def draw(self, xy : ivec) -> None:
        blt.color(self.fg_colour.blt_colour())
        if self.bg_colour is not None:
            blt.bkcolor(self.bg_colour.blt_colour())
        xy = xy + self.xy
        blt.put(xy.x, xy.y, self.char)
PutArgs.__new__.__defaults__ = (ColourRGBA(255,255,255,255),None)

class PutExtArgs(DisplayElement,
                 NamedTuple('PutExtArgs',
                            [('char', Union[int,str]),
                             ('xy', ivec),
                             ('dxy', ivec),
                             ('fg_colour', Colour),
                             ('bg_colour', Optional[Colour])
                            ])):
    def draw(self, xy : ivec) -> None:
        blt.color(self.fg_colour.blt_colour())
        if self.bg_colour is not None:
            blt.bkcolor(self.bg_colour.blt_colour())
        xy = xy + self.xy
        blt.put_ext(xy.x, xy.y, self.dxy.x, self.dxy.y, self.char)
PutExtArgs.__new__.__defaults__ = (ColourRGBA(255,255,255,255),None)

class PrintArgs(DisplayElement,
                NamedTuple('PrintArgs',
                           [('text', str),
                            ('xy', ivec),
                            ('bbox', Optional[ivec]),
                             ('fg_colour', Colour),
                             ('bg_colour', Optional[Colour])
                           ])):
    def draw(self, xy : ivec) -> None:
        blt.color(self.fg_colour.blt_colour())
        if self.bg_colour is not None:
            blt.bkcolor(self.bg_colour.blt_colour())
        xy = xy + self.xy
        if self.bbox is None:
            blt.print_(xy.x, xy.y, self.text)
        else:
            blt.print_(xy.x, xy.y, '[bbox={0}x{1}]'.format(self.bbox.x, self.bbox.y) + self.text)
PrintArgs.__new__.__defaults__ = (None, ColourRGBA(255,255,255,255),None)
