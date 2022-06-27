# count words 'pooh' in 'Winnie the Pooh'
file = 'Winnie-the-Pooh.txt'

with open(file) as f_object:
    lines = f_object.readlines()

text = ''
for line in lines:
    text += line.lower().strip()
    
pooh = text.count('pooh')
print(pooh)


    