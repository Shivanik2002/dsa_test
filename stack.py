List = list()
while True:
    c = int(input(''' 
        1 Push
        2 Pop
        3 Peek
        4 Display
        5 Exit
        '''))
    
    if c == 1:
        n = input("Enter the value")
        List.append(n)
        print(List)
        
    elif c == 2:
        if len(List) == 0:
            print("Empty stack")
        else:
            p = List.pop()
            print(p)
            print(List)
            
    elif c == 3:
        if len(List) == 0:
            print("Empty stack")
        else:
            print("Last stack value",List[-1])
            
    elif c == 4:
        print("Display the stack",List)
        
    elif c == 5:
        break
    else:
        print("Invalid value")                            
        
            