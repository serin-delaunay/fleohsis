
# coding: utf-8
from euclid3 import Vector2 as fvec

class ivec(fvec):
    def __repr__(self) -> str:
        return 'ivec({0}, {1})'.format(self.x, self.y)
