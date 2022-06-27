file = 'pi_million_digits.txt'

with open (file) as f_object:
    lines = f_object.readlines()
    
pi_string =''
for line in lines:
    pi_string += line.strip()
    
birthday = input("Pls enter your birthday date as ddmmyyyy: \n")
if birthday in pi_string:
    print("Yeah - its in Pi!")
else:
    print("Nuh its aint there :(")