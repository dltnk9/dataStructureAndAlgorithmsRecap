class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self
        self.prev = self


class DoublyLinedList:
    def __init__(self):
        self.head = Node()
        self.size = 0


# def __iter__():


# def __str__():
# def __len__():

# splice 연산
# def splice(self, a, b, x):  # 세개의 노드 a,b,x
# 조건 1: a-> ... ->b
# 조건 2 : a와 b사이에 head X
# ap= a.prev, bn= b.next, xn=x.next
# ap.next=bn // cut
# bn.prev=ap // cut

# x.next =a
# a.prev = x
# b.next = xn
# xn.prev = b

# 이동연산
# moveAfter(self,a,x) //  노드a를 노드x 다음으로 이동 == splice(a,a,x) #같은 표현이 된다. in additon to - moveBefore (a,x) a를 x전으로 이동 -> splice(a,a,x.prev)
