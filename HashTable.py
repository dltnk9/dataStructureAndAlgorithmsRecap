# perfect h.f key->slot

# f(k) = k/m - division hash function
# multiplication, folding extraction, additive, patching, universal C

# requirements of hash function
# 1. less collision
# 2. fast compution - trade off

# collision resolution method - open addressing : linear probing 충돌시 아래 슬롯으로 넘어간다.
# quadratic probing 제곱형식으로 - 클러스터가 리니어보단 쌓이지않는다, k-> k+1^2 -> k+2^2 -> k+3^2
# double hashing - 해시함수를 두개를 씀 f(key) -> f(key) + g(key) -> f(key) + 2g(key) -> f(key) + 3g(key)

# cluster - 군집, 슬롯에 데이터 충돌이 많이 나는 곳, 많은 데이터가 집중되는 곳
# chaining

# set,remove, search : cluster size - hash function, collision resolution method, load factor ( n/m) m -slot의 갯수 n h에 저장된 item 갯수 0<n/m<1 n/m = 1/0.5


# Chaining - hash + linked list or doublylinkedlist, O 노테이션 - O(충돌key의평균갯수) - C universal hash function을 쓰면 O(1) 상수를 유지한다
