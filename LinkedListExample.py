# Pseudo Code

class Node:
    def __init(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)


a = Node(3)
b = Node(9)
c = Node(-1)
a.next = b
b.next = c
# 개별적으로 만듦면 노드 수가 많아질수록 비효율적이다. -> 헤드노드 +n - 한방향 연결리스트 객체 만들자, 시간이 오래 걸리더라도 한방향 링크드 리스트의 결점이다


class SignlyLinkedList:  # 빈 리스트 생성
    def __init__(self):
        self.head = None
        self.size = 0

    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = L.head  # 수도 코드이기에 호이스팅 무시
        L.head = new_node
        L.size += 1

    def pushBack(self, key):
        v = Node(key)
        if len(self) == 0:
            self.head = v
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
        tail.next = v
        self.size += 1

    def popFront(self):
        if len(self) == 0:
            return None
        else:  # 하나 이상의 노드가 존재한다.
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x
            return key

    def popBack(self):
        if len(self) == 0:
            return None
        else:  # running technique
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if len(self) == 1:
                self.head = None
            else:
                prev.next = tail.next
            key = tail.key
            del tail
            self.size -= 1
            return key


L = SignlyLinkedList()
L.pushFront(-1)
L.pushFront(9)
L.pushFront(3)
L.pushFront(5)
L.pushBack(4)

# 시간복잡도
# PushFront, PopFront - O(1)
# pushBack PopBack - O(n)
