
sandwich_orders = ['blt', 'pastrami', 'italian', 'hot', 'pastrami', 'mayo', 'pastrami']
finished_sandwiches = []

print("Attencion! - we run out of Pastrami !")

while 'pastrami' in sandwich_orders :
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:    
    sandwich = sandwich_orders.pop()
    print(f"Making your {sandwich} sandwich now ...")
    finished_sandwiches.append(sandwich)
    
print("Your finished sandwiches are: ")
for item in finished_sandwiches:
    print(f" - {item}")
    
    