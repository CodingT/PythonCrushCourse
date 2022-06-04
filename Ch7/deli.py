sandwich_orders = ['blt', 'italian', 'hot', 'mayo']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Making your {sandwich} sandwich now ... \n")
    finished_sandwiches.append(sandwich)
    
print("Here is your finished sanwiches: ")
for sandwich in finished_sandwiches:
    print(f" - {sandwich}")