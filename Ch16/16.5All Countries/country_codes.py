from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for given country"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None # if country not found

#print(get_country_code())


