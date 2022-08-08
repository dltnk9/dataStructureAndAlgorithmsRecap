# sum(n) = 1+2+....+(n-1)+n    - sum(n-1)+n
# 재귀알고리즘(재귀함수) = 알고리즘(함수) 내부에서 한 번 이상 자신의 함수(알고리즘)를 호출

def sum(n):
    if n == 1:
        return 1
    return sum(n-1) + n


# sum(4) =sum(3)+4
# sum(2)+3
# sum(1) +2 - return 1으로 +1+2가 됨 재귀호출.

# 수행시간 : T(n)=T(n-1)+C c는 상수 연산 - 결국 점화식으로 표현된다
# N==1 테스트 - 바닥조건 Base case T(1) = 1 or C
# 2 재귀호출 :T(n)= 점화식


# ex) sum(3,8) = 3+4+5 (sum(3,5))  + 6+7+8 (sum(6,8))
def sum1(a, b):
    if a == b:
        return a
    if a > b:
        return 0
    m = (a+b)//2
    return sum1(a, m)+sum(m+1, b)

# T(n)= T(n) =2*T(n/2)+c
# 단 T(1) = c
# an = 2*a(n/2)+c
