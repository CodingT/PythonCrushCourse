def show_magicians(magicians):
    """Printing passed list"""
    print("\n Here is original list called from function:")
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """Modifying a List"""
    great_magicians = []
    
    while magicians:
        magician = magicians.pop()
        great_magician = f" The Great {magician.title()}!"
        great_magicians.append(great_magician)
    
    #add modified value back to passed to function list !
    for great_magician in great_magicians:
        magicians.append(great_magician)  