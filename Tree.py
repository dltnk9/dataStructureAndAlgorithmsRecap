# Tree 기본 트리는 연결리스트와 같다

# 이진트리 binary tree

# level 0 ~ n , height = level, root node, link edge, leaf node , path

# 1. A= [a, b, c, None ,d, e, f] List
# 2. A = [ a, [b [], d,[],[]], [c,[e,[],[]]], f,[],[]]} left node, right node from the root node
# 3. node def -

# heap - heap property - 모든 부모노드의 KEY값은 자식노드의 KEY값보다 작지않다.

# H[0]의 왼쪽 자식노드 H[1] 오른쪽 자식 노드 H[2] - H[2]의 왼쪽 자식노드 H[2*2+1]=H[5] =E 오른쪽 자식노드 H[2*2+2 ] = H[6] = F, 정리- H[2*K+1] 오른쪽 H[2*K+2]
# H[K]의 부모노드 = H[(K-1)/2]

# O(logn) 1 insert
# O(1) 2 Find-max : return A[0]
# O(logn) 3. delete-max

# make-heap - O(nh) = O(nlogH)
#  heapify-down heapify-up - O(H) = o(logN) - 힙은 인서트 파인드맥스 딜리트맥스에 유용, 서치에는 유용하지않다 - 구조특성상 2개로 나누어짐 search O(1) 이 되려면 하나만 있어야함
