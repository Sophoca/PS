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

