## Print all the nodes of the given tree in inorder tree traversal

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def inOrder(root):
    if root:
        inOrder(root.left)
        print(str(root.data),">-" , end=" ")
        inOrder(root.right)


def preOrder(root):
    if root :
        print(str(root.data),">-",end=" ")
        preOrder(root.left)
        preOrder(root.right)


def postOrder(root):
    if root :
        preOrder(root.left)
        preOrder(root.right)
        print(str(root.data),">-",end=" ")








## Driver code

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder Traversal")
inOrder(root)
print()
print("Preorder Traversal")
preOrder(root)
print()
print("Postorder Traversal")
postOrder(root)
