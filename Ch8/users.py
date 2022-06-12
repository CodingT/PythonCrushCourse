def build_profile(first, last, **other):
    """Function accepts positional and Arbitrary arguments"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in other.items():
        profile['key'] = value
    return profile

user_profile = build_profile('mark', 'smith', age = 25, ocupation = 'it')
print(user_profile)


from functions import make_great as mg

mg(user_profile)