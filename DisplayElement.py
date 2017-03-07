
# coding: utf-8
from typing import NamedTuple, Optional, Union, Iterator, Dict, Callable, Any, TypeVar
from bearlibterminal import terminal as blt
from abc import ABCMeta, abstractmethod
from vec import vec
from Colour import Colour, ColourRGBA
from enum import Enum, auto
from Rectangle import Rectangle

class DisplayElement(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, xy : vec, layer : int = 0) -> None: pass

class PutArgs(DisplayElement,
              NamedTuple('PutArgs',
                         [('char', Union[int,str]),
                          ('xy', vec),
                          ('fg_colour', Colour),
                          ('bg_colour', Optional[Colour])
                         ])):
    def draw(self, xy : vec, layer : int = 0) -> None:
        blt.layer(layer)
        blt.color(self.fg_colour.blt_colour())
        if self.bg_colour is not None:
            blt.bkcolor(self.bg_colour.blt_colour())
        xy = xy + self.xy
        blt.put(xy.x, xy.y, self.char)
PutArgs.__new__.__defaults__ = (ColourRGBA(255,255,255,255),None) # mypy hates this
# When Python 3.6.1 arrives:
#   * Remove __defaults__ assignment
#   * Use class _PutArgs(NamedTuple)
#   * Assign defaults in instance variable type hints
#   * Use class PutArgs(NamedTuple, DisplayElement), to avoid metaclass conflict

class PutExtArgs(DisplayElement,
                 NamedTuple('PutExtArgs',
                            [('char', Union[int,str]),
                             ('xy', vec),
                             ('dxy', vec),
                             ('fg_colour', Colour),
                             ('bg_colour', Optional[Colour])
                            ])):
    def draw(self, xy : vec, layer : int = 0) -> None:
        blt.color(self.fg_colour.blt_colour())
        if self.bg_colour is not None:
            blt.bkcolor(self.bg_colour.blt_colour())
        xy = xy + self.xy
        blt.put_ext(xy.x, xy.y, self.dxy.x, self.dxy.y, self.char)
PutExtArgs.__new__.__defaults__ = (ColourRGBA(255,255,255,255),None) # mypy hates this
# When Python 3.6.1 arrives:
#   * Remove __defaults__ assignment
#   * Use class _PuExttArgs(NamedTuple)
#   * Assign defaults in instance variable type hints
#   * Use class PutExtArgs(NamedTuple, DisplayElement), to avoid metaclass conflict

class TextAlignmentH(Enum):
    Left = blt.TK_ALIGN_LEFT
    Centre = blt.TK_ALIGN_CENTER
    Right = blt.TK_ALIGN_RIGHT
    Default = blt.TK_ALIGN_DEFAULT
class TextAlignmentV(Enum):
    Top = blt.TK_ALIGN_TOP
    Middle = blt.TK_ALIGN_MIDDLE
    Bottom = blt.TK_ALIGN_BOTTOM
    Default = blt.TK_ALIGN_DEFAULT

class TextAlignment(NamedTuple('TextAlignment', [('horizontal', TextAlignmentH), ('vertical', TextAlignmentV)])):
    def code(self) -> int:
        return self.horizontal.value + self.vertical.value
TextAlignment.__new__.__defaults__ = (TextAlignmentH.Default, TextAlignmentV.Default) # mypy hates this
# When Python 3.6.1 arrives:
#   * Remove __defaults__ assignment
#   * Use class TextAlignment(NamedTuple)
#   * Assign defaults in instance variable type hints

class PrintArgs(DisplayElement,
                NamedTuple('PrintArgs',
                           [('text', str),
                            ('xy', vec),
                            ('bbox', Optional[vec]),
                            ('align_h', TextAlignmentH),
                            ('align_v', TextAlignmentV),
                            ('fg_colour', Colour),
                            ('bg_colour', Optional[Colour])
                           ])):
    def draw(self, xy : vec, layer : int = 0) -> None:
        blt.color(self.fg_colour.blt_colour())
        if self.bg_colour is not None:
            blt.bkcolor(self.bg_colour.blt_colour())
        xy = xy + self.xy
        if self.bbox is None:
            blt.print_(xy.x, xy.y, self.text)
        else:
            blt.print_(xy.x, xy.y, self.text, self.bbox.x, self.bbox.y, self.align_h.value + self.align_v.value)
PrintArgs.__new__.__defaults__ = (None, TextAlignmentH.Default, TextAlignmentV.Default, 
                                  ColourRGBA(255,255,255,255),None) # mypy hates this
# When Python 3.6.1 arrives:
#   * Remove __defaults__ assignment
#   * Use class _PrintArgs(NamedTuple)
#   * Assign defaults in instance variable type hints
#   * Use class PrintArgs(NamedTuple, DisplayElement), to avoid metaclass conflict

T = TypeVar('T',bound='Clickable')
class Clickable(object):
    def __init__(self, element : DisplayElement,
                 mouse_rect : Rectangle = Rectangle(vec(0,0), vec(0,0)),
                 signals : Dict[str, Callable[[vec,int,Dict[str,Any]],Any]] = {}) -> None:
        self.element = element
        self.mouse_rect = mouse_rect
        self.signals = signals.copy()
    def find_target(xy : vec, signal : int) -> Optional[T]:
        if xy in self.mouse_rect:
            if isinstance(self.element, DisplayGroup):
                for clickable in self.element:
                    result = clickable.find_target(xy - self.mouse_rect.top_left)
                    if result is not None:
                        return result
            if signal in self.signals:
                return self
        return None

class DisplayGroup(DisplayElement, metaclass=ABCMeta):
    def __init__(self, xy : vec) -> None:
        self.clear_elements()
        self.layer = 0
        self.xy = xy
    def draw(self, xy : vec, layer : int = 0) -> None:
        xy = self.xy + xy
        for clickable in self:
            element = clickable.element
            if isinstance(element, DisplayGroup):
                element.draw(xy, layer + 1)
            else:
                element.draw(xy, layer)
    @abstractmethod
    def clear_elements(self) -> None: pass
    @abstractmethod
    def __iter__(self) -> Iterator[Clickable]: pass

class DisplayList(DisplayGroup):
    def clear_elements(self) -> None:
        self.elements = []
    def __iter__(self) -> Iterator[Clickable]:
        return iter(self.elements)

class DisplayDict(DisplayGroup):
    def clear_elements(self) -> None:
        self.elements = {}
    def __iter__(self) -> Iterator[Clickable]:
        return iter(self.elements.values())
