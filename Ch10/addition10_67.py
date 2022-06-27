
while True:
    print("Adition calculator, enter 'Ctl+C' to quit")
    try:
        first_num = int(input("Enter first number:\n"))
        second_num = int(input("Enter second number:\n"))
        answer = first_num + second_num
    except ValueError:
        print("Make sure you entered a number") 
    else:    
        print(f"{first_num}+{second_num}={answer}")
