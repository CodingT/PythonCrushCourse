words = {'boolean': 'true or false',
         'tuple': 'data type stored multiple ordered, unchangible values',
         'list': 'data type' }

#print(words)

word = 'tuple'
print(f"{word} : is a {words['tuple']}.")

for key, value in words.items():
    print(f"{key.title()} - {value}. \n")