class Stack:
    def __init__(self):
        self.items = []  # 데이터 저장을 위한 리스트 준비

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:  # pop 할 아이템이 없으면
            return self.items.pop()
        except IndexError:  # index error 발생
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):  # len()로 호출하면 stack의 item 수 반환
        return len(self.items)


S = Stack()
S.push(10)
S.push(2)
print(S.pop())
print(S.top())

# 괄호 맞추기

# for p in parseg :
# if p == `(` : S.push(p)
# elif p == `)` : S.pop()
# else : print("not allowed symbol")

# if len(S) > 0 : return false
# else : return True
