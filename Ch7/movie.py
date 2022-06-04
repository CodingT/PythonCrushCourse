#Version 1
#age = int(input("Please enter your age: \n"))

#if age <= 3:
#    print("For 3 and younger, enter is free")
#elif age <= 12:
#    print("Your ticket is $10")
#else: 
#    print("Your tidket is $15")
 
 
 #Version 2:   
while True:
    age = input("Please enter your age or 'quit' to exit: \n")
    if age == 'quit':
        break
    elif int(age) < 3:
        print("Your enter is free")
    elif int(age) <= 12:
        print("Your ticket will be $10")
    else:
        print("Your ticket is $15")
    
    