file = 'learningPython.txt'

with open(file) as f_object:   
   # content = f_object.read()   #1
   # print(content.strip())

   # for line in f_object:        #2
     #  print(line.strip())
     
     lines = f_object.readlines()  #3


for line in lines:
    print(line.strip())   
   