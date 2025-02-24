# Binary Tree Traversal Repository

This repository contains a Python implementation of basic **Binary Tree Traversal** techniques using a simple binary tree structure.

## Files Included

### 1. **level_order.py**
   - This file is intended to include an implementation of **Level Order Traversal**, a breadth-first traversal technique for binary trees. (Note: The content of this file can be added based on your implementation).

### 2. **traversal.py**
   - This file demonstrates different traversal techniques for a binary tree, including:
     - **Inorder Traversal**: Visits nodes in the order: Left, Root, Right.
     - **Preorder Traversal**: Visits nodes in the order: Root, Left, Right.
     - **Postorder Traversal**: Visits nodes in the order: Left, Right, Root.

## Code Explanation

### `Node` Class:
- Defines the structure of a tree node with:
  - `val`: The value of the node.
  - `left`: Left child node.
  - `right`: Right child node.

### `BinaryTree` Class:
- Contains the root node of the binary tree and a constructor for initializing the tree with the root value.
  
### Traversal Functions:
- **In-order Traversal**: Left → Root → Right.
- **Pre-order Traversal**: Root → Left → Right.
- **Post-order Traversal**: Left → Right → Root.

### Example:
```python
# Create a binary tree
tree = BinaryTree(7)
tree.root.left = Node(26)
tree.root.right = Node(31)
tree.root.left.left = Node(12)
tree.root.left.right = Node(55)
tree.root.right.left = Node(61)
tree.root.right.right = Node(37)

# Perform traversals
print("Inorder Traversal:")
tree.root.in_order_traversal()
print("\nPreorder Traversal:")
tree.root.pre_order_traversal()
print("\nPostorder Traversal:")
tree.root.post_order_traversal()
