from __future__ import annotations
from node import Node, Color


class RedBlackTree:
    def __init__(self):
        self.sentinel = Node(value=0, color=Color.BLACK)
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel
        self.sentinel.parent = self.sentinel
        self.root = self.sentinel

    def insert(self, value: int):
        my_Node = Node(value, color=Color.RED, left=self.sentinel, right=self.sentinel, parent=self.sentinel)

        x = self.root
        px = self.sentinel

        while x != self.sentinel:
            px = x
            if x.value < my_Node.value:
                x = x.right
            else:
                x = x.left

        my_Node.parent = px

        if px == self.sentinel:
            self.root = my_Node
        else:
            if px.value < my_Node.value:
                px.right = my_Node
            else:
                px.left = my_Node
        self.fixColorAfterInsertion(my_Node)

    def fixColorAfterInsertion(self, node: Node):
        while node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y != self.sentinel and y.color == Color.RED:
                    node.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotateLeft(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.rotateRight(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y != self.sentinel and y.color == Color.RED:
                    node.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotateRight(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.rotateLeft(node.parent.parent)

        self.root.color = Color.BLACK

    def rotateRight(self, node: Node):
        leftNode = node.left
        node.left = leftNode.right

        if leftNode.right != self.sentinel:
            leftNode.right.parent = node

        leftNode.parent = node.parent

        if node.parent == self.sentinel:
            self.root = leftNode
        else:
            if node == node.parent.right:
                node.parent.right = leftNode
            else:
                node.parent.left = leftNode

        leftNode.right = node
        node.parent = leftNode

    def rotateLeft(self, node: Node):
        rightNode = node.right
        node.right = rightNode.left

        if rightNode.left != self.sentinel:
            rightNode.left.parent = node

        rightNode.parent = node.parent

        if node.parent == self.sentinel:
            self.root = rightNode
        else:
            if node == node.parent.left:
                node.parent.left = rightNode
            else:
                node.parent.right = rightNode

        rightNode.left = node
        node.parent = rightNode

    def search(self, val: int):
        current = self.root
        while current !=self.sentinel and current.value != val:
            if val < current.value:
                current = current.left
            else:
                current = current.right
        return current

    def _minimum(self,node: Node)->Node:
        while node.left != self.sentinel:
            node = node.left
        return node

    def _transplant(self, node: Node, newNode: Node):
        if node.parent == self.sentinel:
            self.root = newNode
        else:
            if node.parent.left==node:
                node.parent.left=newNode
            else:
                node.parent.right=newNode
        newNode.parent=node.parent

    def delete(self,val: int):
        current = self.search(val)

        if(current==self.sentinel):
            raise ValueError("Value not found")

        current_color=current.color

        if(current.left==self.sentinel and current.right!=self.sentinel):
            x=current.right
            self._transplant(current, current.right)

        elif(current.right==self.sentinel and current.left!=self.sentinel):
            x=current.left
            self._transplant(current, current.left)

        else:
            y=self._minimum(current.right)
            y_color=y.color
            x=y.right
            if(y.parent ==current):
                x.parent=y
            else:
                self._transplant(y, y.right)
                y.right=current.right
                y.right.parent=y
            self._transplant(current, y)
            y.left=current.left
            y.left.parent=y
            y.color=current.color

        if(current_color==Color.BLACK):
            self.fixup(x)

    def _delete_fixup(self,node: Node):
        #TODO:
        raise NotImplementedError()

