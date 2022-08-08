# Binary Search Tree (BST)
# 이진탐색트리 조건 1. 각 노드의 왼쪽 subtree의 key값은 노드의 key값보다 작거나 같아야하고 오른쪽 subtree의 key 값은 노드의 key값보다 커야한다
# O(h) - 레벨을 최대한 낮게 유지해야 알고리즘 효율적

from curses import keyname


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()  # iterator, Generator
    T = BST()
    T.insert(15)
    T.insert(4)

    def find_loc(self, key):  # key값 노드가 있다면 해당 노드 return, 없다면 노드가 삽입할 부모노드 리턴
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v != None:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p

    def search(self, key):
        r = self.find_loc(key)
        if v == None:
            return None
        else:
            return v

    def insert(self, key)
    p = self.find.loc(key)
    if p == None or p.key != key:
        v = Node(key)
        if p == None:
            self.root = v
        else:
            p != None, p.key != keyname
            v.parent = p
            if p.key >= key:
                p.left = v
            else p.right = v
        self.size += 1
        return v
    else:
        print("Key is alredy there")
        return p  # p=None
# 트리가 작으면 작을수록 인서트 빠르다
