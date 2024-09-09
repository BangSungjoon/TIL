'''
7
3 5 1 2 7 4 -5
'''

# 이진 탐색 트리 노드 클래스 정의
class Node:
    def __init__(self, key):
        self.key = key  # 노드의 값
        self.left = None  # 왼쪽 자식 노드 초기화
        self.right = None  # 오른쪽 자식 노드 초기화

# 이진 탐색 트리 클래스 정의
class BinarySearchTree:
    def __init__(self):
        self.root = None  # 트리의 루트(root) 노드를 None으로 초기화

    # 트리에 값을 삽입하는 메서드
    def insert(self, key):
        if self.root is None:  # 루트가 비어있으면
            self.root = Node(key)  # 새로운 노드를 루트로 설정
        else:
            self._insert(self.root, key)  # 루트가 있으면 재귀적으로 삽입 위치를 찾아 삽입

    # 재귀적으로 삽입 위치를 찾는 헬퍼 메서드
    def _insert(self, node, key):
        if key < node.key:  # 삽입하려는 값이 현재 노드의 값보다 작으면
            if node.left is None:  # 왼쪽 자식이 비어있다면
                node.left = Node(key)  # 왼쪽 자식에 새로운 노드를 추가
            else:
                self._insert(node.left, key)  # 왼쪽 자식 노드로 이동하여 다시 삽입 시도
        else:  # 삽입하려는 값이 현재 노드의 값보다 크거나 같으면
            if node.right is None:  # 오른쪽 자식이 비어있다면
                node.right = Node(key)  # 오른쪽 자식에 새로운 노드를 추가
            else:
                self._insert(node.right, key)  # 오른쪽 자식 노드로 이동하여 다시 삽입 시도

    # 트리에서 특정 값을 검색하는 메서드
    def search(self, key):
        return self._search(self.root, key)  # 루트 노드부터 검색 시작

    # 재귀적으로 특정 값을 검색하는 헬퍼 메서드
    def _search(self, node, key):
        if node is None or node.key == key:  # 노드를 찾았거나 더 이상 노드가 없으면
            return node  # 현재 노드를 반환 (None일 수도 있음)
        if key < node.key:  # 찾으려는 값이 현재 노드의 값보다 작으면
            return self._search(node.left, key)  # 왼쪽 자식 노드로 이동하여 다시 검색
        else:  # 찾으려는 값이 현재 노드의 값보다 크면
            return self._search(node.right, key)  # 오른쪽 자식 노드로 이동하여 다시 검색

    # 중위 순회를 수행하는 메서드 (작은 값부터 큰 값 순으로 출력됨)
    def inorder_traversal(self):
        self._inorder_traversal(self.root)  # 루트 노드부터 중위 순회 시작

    # 재귀적으로 중위 순회를 수행하는 헬퍼 메서드
    def _inorder_traversal(self, node):
        if node:  # 현재 노드가 None이 아닐 때
            self._inorder_traversal(node.left)  # 왼쪽 자식 노드를 먼저 방문
            print(node.key, end=' ')  # 현재 노드의 값을 출력
            self._inorder_traversal(node.right)  # 오른쪽 자식 노드를 방문

# 입력 받기
N = int(input())  # 입력받은 숫자 개수
arr = list(map(int, input().split()))  # 입력받은 숫자 리스트

bst = BinarySearchTree()  # 이진 탐색 트리 객체 생성

# 입력받은 숫자를 트리에 삽입
for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회를 통해 트리의 값을 오름차순으로 출력

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")

