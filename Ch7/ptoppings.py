
prompt = "\n Please chose your topping, or type 'quit' to stop:"

toppings = []


active = True
while active :
    message = input(prompt)
    if message == 'quit':
        active = False
    else:    
        print(f"You have added {message}")
        toppings.append(message)
    
print("You have order a pizza with:")
for toping in toppings:
    print(f"- {toping} \n")