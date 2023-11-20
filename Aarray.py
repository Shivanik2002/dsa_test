# from array import *
# arrayName = array(typecode, [Initializers])

from array import *

array1 =  array('i',[10,20,30,40,50])
print(len(array1))
for r in array1:
    print(r)

print()
    
print(array1[0])
print(array1[1])    

print("_________________________|Insertion Operation|____________________________")
 
array1.insert(5,60)
array1.insert(6,80)
array1.insert(6,70)
for x  in array1:
    print(x)
    
print("_________________________|Deletion Operation|____________________________")

array2 = array('i',[1,2,3,4,9,4,5,6])  
array2.remove(4)   
array2.remove(9)
for i in array2:
    print(i)
    
print("_________________________|Search Operation|____________________________")

print(array2.index(5))
print(array2.index(1))

print("_________________________|Update Operation|____________________________")

Array3 = array('i',[2,4,6,8,10,11,14,16,18,40])

Array3[5] = 12
Array3[9] = 20    

for i in Array3:
    print(i)
