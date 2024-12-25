class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    
    if node is None:
        return []
    
    return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = preorder_traversal(root)
print(f"Preorder traversal of the binary tree: {result}")
