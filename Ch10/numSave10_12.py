import json

fileName = 'ssaveNum.json'

try:
    with open(fileName) as f_obj :
        num = json.load(f_obj)
        
except FileNotFoundError:
    num = input(f"Whats your favorite number? ")
    with open(fileName, 'w') as f_obj :
        json.dump(num, f_obj)
        print(f"We have remember your fav num:  {num} .")
        
else:
    print(f"We know your fav num is: {num} !")        


