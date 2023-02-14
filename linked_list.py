class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        print(self.dataval)
        self.nextval = None
        
class Linked_List:
    def __init__(self):
        self.headval = None

list1 = Linked_List()
list1.headval = Node("Monday")
e2 = Node("Tuesday")       
e3 = Node("Wednesday")

# Link first Node to decond node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

obj1 = Node(2)
obj2 = Linked_List()
