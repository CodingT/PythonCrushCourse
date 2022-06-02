guests = ['johny', 'marko', 'poulie', 'frankie']

msg = f"How you doin {guests[0].title()}! Come over to dinner!"
print (msg) 

msg = f"Unfortunately {guests[1].title()} is not gonna make it!"
print(msg)
del guests[1]
guests.insert(1, 'tony')

msg = f"{guests[1].title()} will join us tonight!"
print (msg)

guests.insert(0, 'vincent')
guests.insert(2, 'gary dark')
guests.append('francis')

print(guests)
msg = ("\noh no - enough food only for two persons")
print (msg)
print (f"Sorry {guests.pop()}, {guests.pop()}, {guests.pop()} no food for you ")

print(f"\n total is {len(guests)} invited to diner")

print(f"this is empty list {guests.clear()} otakoi")
print(guests)