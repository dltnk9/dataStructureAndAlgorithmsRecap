class Queue:
    def __init__(self):
        self.items = []  # 빈 리스트
        self.front_index = 0

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index == len(self.items):
            print("Q is empty")
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x

# Josephus problem
# pseudo code
# Josephus(n,k):
# return 최종생존자의번호

# n=9, k=3
# dequeue enqueue, dequeue enqueue, dequeue
