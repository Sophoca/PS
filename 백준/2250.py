class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def count_left(self, count=0):
        if self.left:
            print("left", self.data, count)
            return tree[self.left].count_left(count + 1) + tree[self.left].count_right(count)
        else:
            print("left", count)
            return count

    def count_right(self, count=0):
        if self.right:
            print("right", self.data, count)
            return tree[self.right].count_left(count) + tree[self.right].count_right(count + 1)
        else:
            print("right", count)
            return count


N = int(input())
tree = dict()
for _ in range(N):
    root, left, right = map(int, input().split())
    node = Node(root)
    if left != -1:
        node.left = left
    if right != -1:
        node.right = right
    tree[root] = node

print(tree[1].count_left())
