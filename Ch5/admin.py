
username = input('Please type your username: ')

#usernames = [] # 'user', 'secretary', 'admin', 'service'
if username:    
    if username == 'admin':
        print(f"You have logged in as {username} - privilaged user, pls be be cariful!")
    elif username == 'service':
        print(f"You logged in as {username} account, with limited access.")
    else:
        print(f"Hello {username}!")
else:
    print("Username is required!")


