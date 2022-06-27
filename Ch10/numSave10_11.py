import json
import time

numFile = 'saveNum.json'
favNum = input("Pls enter your number: \n")

with open(numFile, 'w' ) as f_object:
    json.dump (favNum, f_object)
    
        
time.sleep(3)
with open(numFile) as f_object:
    yourNum = json.load(f_object)
print(f"I know yoour favorite number is: {yourNum} !")    

    