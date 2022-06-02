rivers = {'egypt': 'nile',
          'brazil': 'amazon',
          'united states': 'missisipi' }

for key, value in rivers.items():
    print( value.title())
    print(f"{value.title()} is runs trough {key.title()}.")
    print(key.title() + "\n")
    
#print(rivers.values())

for river in rivers.values():
    print(river.title())
print('\n')    
for country in rivers.keys():   # python runnig for dictionaries keys by default
    print( country.title())    