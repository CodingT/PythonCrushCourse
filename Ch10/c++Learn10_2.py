pfile = 'learningPython.txt'
cfile = 'learningCpp.txt'

with open(pfile) as f_object:
    content = f_object.readlines()
    
with open(cfile, 'w') as f_object:
    for line in content:
        f_object.write(line.replace('Python', 'C++'))
        
with open(cfile) as f:
    content = f.read()
print(content)
print(type(cfile))

# rewrite with  'r+'  - read and write