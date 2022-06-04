people = ['tony', 'michael', 'sammy']
took_poll = []
responses = {}

while people:
    name = people.pop()
    response = input(f"Hi {name.title()}, whats your dream vacation? \n")
    responses[name] = response
    took_poll.append(name)
        
#print(responses)
        
for name, response in responses.items():
    print(f"\n {name.title()}'s favorite vacation will be {response.title()} !")    
