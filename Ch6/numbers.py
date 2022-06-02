numbers = {'jack': [5, 9, 3],
           'michael': [7, 22, 11],
           'harry': [7],
           'nick': [14, 99, 69] }

#print("Jacks favorite number is " + str(numbers['jack']))
#print(numbers['michael'])
#print(numbers['harry'])
#print(numbers['nick'])

#for key, value in numbers.items():
 #   print(key.title(), value)
    
#numbers['smith'] = 77

#print(numbers['smith'])

#for key, value in numbers.items():
 #   if key == 'smith':
  #      print(key.title(), value)
  
for key, values in numbers.items():
    print(f" {key.title()} favorite numbers are:")
    for value in values:
        print(f" {value}")