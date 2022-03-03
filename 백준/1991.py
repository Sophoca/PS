# 트리 순회
# 트리, 구현

# 전위 순회: root -> left child -> right child
# 중위 순회: left child -> root -> right child
# 후위 순회: left child -> right child -> root

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return self.data

    def pre_print(self):
        print(self.data, end="")
        if self.left:
            tree[self.left].pre_print()
        if self.right:
            tree[self.right].pre_print()

    def middle_print(self):
        if self.left:
            tree[self.left].middle_print()
        print(self.data, end="")
        if self.right:
            tree[self.right].middle_print()

    def post_print(self):
        if self.left:
            tree[self.left].post_print()
        if self.right:
            tree[self.right].post_print()
        print(self.data, end="")


N = int(input())
tree = dict()
for _ in range(N):
    a, b, c = map(str, input().split())
    node = Node(a)
    if b != ".":
        node.left = b
    if c != ".":
        node.right = c
    tree[a] = node

tree["A"].pre_print()
print()
tree["A"].middle_print()
print()
tree["A"].post_print()