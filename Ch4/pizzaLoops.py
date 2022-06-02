


pizzas = ['dominos', 'papa johns', 'dante', 'paperonni', 'dyadka toni']
#for pizza in pizzas:
 #   print(f"\nMy favorite pizzas is {pizza}.")
    
#print ("\n yeah i like all pizzas")

#print(f"The last three items in the list are: {join(pizzas[-3:])} pizzas")
#4-10
print(len(pizzas))
print("middle three pizzas are:")
for i in pizzas[1:4]:
    print(i)
  
#4.11  
frined_pizzas = pizzas[:]
pizzas.append('hawai')
frined_pizzas.append('jackSlam')
print('\nMy favorite pizza are: ')
for i in pizzas:
    print(i)
print("\nMy friend pizzas are: ")
for i in frined_pizzas:
    print(i)