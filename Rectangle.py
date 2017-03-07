
# coding: utf-8
import itertools as it
from typing import NamedTuple
from vec import ivec
from enum import Enum

class RectangleEdgeH(Enum):
    Left = 0
    Centre = 1
    Right = 2
class RectangleEdgeV(Enum):
    Top = 0
    Middle = 3
    Bottom = 6

class RectangleEdge(NamedTuple):
    horizontal : RectangleEdgeH
    vertical: RectangleEdgeV

class Rectangle(NamedTuple('Rectangle',[('top_left',ivec),('size',ivec)])):
    def bottom_right(self):
        return self.top_left + self.size
    def __contains__(self, xy):
        return self.contains(xy)
    def contains(self, xy):
        return (self.top_left.x <= xy[0] < self.top_left.x + self.size.x and
                self.top_left.y <= xy[1] < self.top_left.y + self.size.y)
    def contains_rectangle(self, other):
        return (self.top_left.x <= other.top_left.x and
                self.top_left.y <= other.top_left.y and
                self.bottom_right().x >= other.bottom_right().x and
                self.bottom_right().y >= other.bottom_right().y)
    def copy(self, f=lambda x: x.copy()):
        return Rectangle(f(self.top_left),f(self.size))
    def border_code(self, xy):
        if xy.x == self.top_left.x:
            h = RectangleEdgeH.Left
        elif xy.x == self.top_left.x+self.size.x-1:
            h = RectangleEdgeH.Right
        else:
            h = RectangleEdgeH.Centre
        if xy.y == self.top_left.y:
            v = RectangleEdgeV.Top
        elif xy.y == self.top_left.y+self.size.y-1:
            v = RectangleEdgeV.Bottom
        else:
            v = RectangleEdgeV.Middle
        return RectangleEdge(h,v)
    def __iter__(self):
        br = self.bottom_right()
        return (ivec(x,y) for (x,y) in it.product(range(self.top_left.x, br.x),
                                                  range(self.top_left.y, br.y)))
    def iter_codes(self):
        br = self.bottom_right()
        for (x,y) in it.product(range(self.top_left.x, br.x),
                                range(self.top_left.y, br.y)):
            yield (ivec(x,y), self.border_code(ivec(x,y)))

