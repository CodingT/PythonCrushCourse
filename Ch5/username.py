new_username = input('Please enter your username:').lower()
current_users = ['admin', 'root', 'service', 'alex', 'kevin']
#new_user = ['michael', 'sam', 'roots', 'simon', 'igor']

#for user in new_username:
if new_username in current_users:
    print(f"{new_username} username is already exist, chose another one")
else:
    print(f"{new_username} is available.")    