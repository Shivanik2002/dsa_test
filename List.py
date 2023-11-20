# Python - Lists

list = ["Shreya","Nitya",2000,13.45]
list1 = [1,2,3,4,5,6,7,8]
print(list)
print(list1)

print("_____________________________Accessing Values_________________________")

x = list[3]
print("List[3] :" ,x)

print("list1[0:4] :", list1[0:4])

print("_____________________________Updating Lists_________________________")

Lst = [123,456,789,"Shivani","3+7i",123.4]
print(Lst)

print("Value available at index 2 : ")
print(Lst[2])

Lst[2] = "Saloni"
print("New value available at index 2 : ")
print(Lst[2])

# Append Method
Lst.append("Kushwah")
print("After added the element in a Lst with the help of append() :", Lst)

print("____________________________Delete List Elements_________________________")

list1 = ['physics', 'chemistry', 1997, 2000,1998]
print (list1)

del list1[2]
print ("After deleting value at index 2 : ")
print (list1)

# Remove Method
list1.remove(1998)
print(list1)

print("___________________________Basic List Operations_________________________")

lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10] 
print(len(lst1))    #Length Method

print(lst1+lst2)   # Concatenation

print(['Hii'] * 4)  # Repetition

print(3 in [1,2,3,4,5])  # Membership

for i in lst1:     #Iteration
    print(i)