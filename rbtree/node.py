from __future__ import annotations
from enum import Enum,auto
class Color(Enum):
    RED = auto()
    BLACK = auto()

class Node:
    def __init__(self, value,color:Color, left:Node=None, right:Node=None,parent:Node=None):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent



