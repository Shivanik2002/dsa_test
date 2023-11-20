List = list()
while True:
    
    c = int(input('''
        1 Push elements
        2 Pop elements
        3 Front element
        4 Last element  
        5 Display Queue
        6 Exit
        '''))
    if c == 1:
      n = (input("Enter the value : "))
      List.append(n)
      print(List)
    
    elif c == 2:
      if len(List) == 0:
        print("Empty queue")
      else:
        p = List.pop()
        print(p)
        print(List)
    
    elif c == 3:
       if len(List) == 0:
        print("Empty queue")
       else:
         print("Front queue value ", List[0])
    elif c == 4:
       if len(List) == 0:
        print("Empty queue")
       else:
         print("Last queue value ",List[-1]) 
    
    elif c == 5:
      print("Display Queue")
      
    elif c == 6:
      break
    else:
      print("Invalid Queue")  
               
              