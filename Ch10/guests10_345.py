guestfile = 'guests.txt'
answersfile = 'answers.txt'
    
while True:    
     name = input("Please enter your name:\n")
     print(f"Hello {name.title()}!")
     with open(guestfile, 'a') as f_object:
         f_object.writelines(f"{name.title()} \n")
     
     answer = input(f"{name.title()}, please tell me, why do you like programming?\n")
     with open(answersfile, 'a') as f_object:
         f_object.writelines(f"{name.title()} like programming because: {answer}. \n")
         
    
    
