from random import choice

random_list = [0,1,2,3,4,5,6,7,8,9,'a','b','c','e','f']

winners = []

for i in range(4):
    winners.append(random.choice(random_list))

print(f"And the winner is :") 
print(*winners)

