def city_count_pop (city, country, population=''):
    """Def function"""
    if population:
        full_name = f"{city.title()}, {country.title()} - population is {population}."
    else: 
        full_name = f"{city.title()}, {country.title()}"
    return full_name



#test = city_count_pop('kiev', 'ukraine', 500000)
#print(test)