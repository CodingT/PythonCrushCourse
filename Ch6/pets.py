pets = []

pet_1 = {'kind': 'dog', 'name':  'rex', 'owner': 'mike' }
pets.append(pet_1)
pet_2 = {'kind': 'cat', 'name':  'tigra', 'owner': 'tony' }
pets.append(pet_2)
pet_3 = {'kind': 'hamster', 'name':  'kush', 'owner': 'lissa' }
pets.append(pet_3)


for pet in pets:
    print(f" \n {pet['owner'].title()} have a {pet['kind']}, and its name is {pet['name'].title()}.")