
person_1 = {'first_name': 'michael',
          'last_name': 'jackson',
          'age': 35,
          'city': 'NY'}
person_2 = {'first_name': 'sam',
            'last_name': 'smith',
            'age': 33,
            'city': 'miami'}
person_3 = {'first_name': 'jack',
            'last_name': 'shmack',
            'age': 19,
            'city': 'dallas'}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city']
    
    print(f"\n {full_name} from {city.title()} is {age} years old.")

