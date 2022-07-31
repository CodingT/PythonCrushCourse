#Function that take list as argument and return it as string
#with all items separated by comma and space, with 'and' before last item
def commaCode(list):
    """Func definition"""
    strList = (', '.join(list[:-1]))
    lastItem = (''.join(list[-1]))
    print(f"{strList}, and {lastItem}")


pets = ['perrot', 'fish', 'dog', 'cat', 'hamster']

commaCode(pets)
commaCode(pets[:3])
