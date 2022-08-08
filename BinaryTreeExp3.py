# expression 1 - binary tree - > list. array ex) heap
# expression 3 - using node and link

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)

    def preorder(self):  # 현재방문중인노드 =self
        if self != None:
            print(self.key)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
                # 재귀적으로 호출한다. recursive


a = Node(6)
b = Node(9)
c = Node(1)
d = Node(5)

a.left = b
a.right = c
b.parent = c.parent = a
b.right = d
d.parent = b

# 순회 traversal - preorder inorder, postorder - 이진트리 노드 key값을 빠짐없이 출력하는 방법

# left subtree right subtree
# M ROOT, L LEFT SUBTREE, R RIGHT SUBTREE
#preorder - MLR , inorder - LMR, postorder - LRM

# reconstruct
#preorder :FBADCEGIH
#inorder : ABCDEFGHI
