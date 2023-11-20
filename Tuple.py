tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

# Empty Tuple
# tup1 = (50,)

print("_______________________________Accessing Values in Tuples____________________________")

print("tup1[0] : ",tup1[0])
print("tup1[0:3] :",tup1[0:3])

print("_______________________________Updating Tuples______________________________")

tuple1 = (12, 34.56)
tuple2 = ('abc', 'xyz')

# this action is not valid for tuples
# tuple1[0] = "Shivani"

tuple3 = tuple1 + tuple2
print(tuple3)

print("______________________________Delete Tuple Elements______________________________")

print(tuple3)
del tuple3
# print("After deleting tup : ")
# print(tuple3)

print("___________________________Basic List Operations_________________________")

tupl1 = (1,2,3,4,5)
tupl2 = (6,7,8,9,10) 
print(len(tupl1))    #Length Method

print(tupl1+tupl2)   # Concatenation

print(('Hii',) * 4)  # Repetition

print(3 in (1,2,3,4,5))  # Membership

for i in tupl1:     #Iteration
    print(i)