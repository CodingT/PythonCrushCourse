cities = {'new york': {'country': 'usa', 'population': '10m', 'fact': 'never sleep'},
          'london': {'country': 'uk', 'population': '6m', 'fact': 'capital of great britan'},
          'paris': {'country': 'france', 'population': '5m', 'fact': 'see and die'}
          }
for city, staff in cities.items():
    print( f" \n {city.title()} is in {staff['country'].title()} have about {staff['population']} people, and it's a {staff['fact']}.")