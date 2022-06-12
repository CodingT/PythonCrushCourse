def make_sendwich(*items):
    """Function accepting any number of parameters"""
    print(f"\nHere is your Sanwitch with:")
    for item in items:
        print("- " + item)

#ingredients = ('onion', 'ketchup', 'mayo', 'ham')
make_sendwich ('onion', 'ketchup', 'mayo', 'ham')
make_sendwich ('sausage', 'spinach', 'mustard')