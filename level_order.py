class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root_val, left=None, right=None):
        self.root = Node(root_val, left, right)

    def level_order_traversal(self):
        queue = [self.root]
        while len(queue) > 0:
            curr = queue.pop(0)
            print(curr.val, end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

# Example usage:
tree = BinaryTree(10,
    left=Node(20,
        left=Node(40),
        right=Node(50)),
    right=Node(30,
        left=Node(60),
        right=Node(70)))

print("Level Order Traversal:")
tree.level_order_traversal()

