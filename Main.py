total = 0
for x in range (10):
    print ("Enter your last score")
    throw = int(input())
    throw2 = 0
    throw3 = 0
    if throw < 10:
        throw2 = int (input("Enter your last score")) 
    frame = throw + throw2    
    if frame < 10:
        throw3 = int (input("Enter your last score")) 
    frame = throw + throw2 + throw3
    print (frame)
    total = total + frame
    print (total)



    