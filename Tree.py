class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
    def insertnode(self,data):
        if data is None:
            self.data=data
        else:
# Here, we compare the new data with the current node's data
            if data < self.data:
#If the left child is empty, insert the data as the left child
                if self.left is None:
                    self.left=Node(data)
#If the left child is not empty, recursively insert the data into the left subtree
                else:
                    self.left.insertnode(data)
            else:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insertnode(data)

#inorder prints first left then root then right
def print_inorder(r):
    if r is None:
        return
    else:
        print_inorder(r.left)
        print(r.data,end='->')
        print_inorder(r.right)

def print_preorder(r):
    if r is None:
        return
    else:
        print(r.data,end='->')
        print_preorder(r.left)
        print_preorder(r.right)

def print_postorder(r):
    if r is None:
        return
    else:
        print_postorder(r.right)
        print(r.data,end='->')
        print_postorder(r.left)

root=Node('g')
root.insertnode('b')
root.insertnode('c')
root.insertnode('a')
root.insertnode('f')
root.insertnode('k')
root.insertnode('j')
root.insertnode('e')
root.insertnode('h')
root.insertnode('d')
root.insertnode('i')
print_inorder(root)
print()
print_preorder(root)
print()
print_postorder(root)