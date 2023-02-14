class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):

# compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)                   
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data) 
        else:
            self.data = data

# Print the tree 
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()                


print("___________________________")
print("___________________________________")

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data) 

    root = Node(10)
    root.PrintTree()       
