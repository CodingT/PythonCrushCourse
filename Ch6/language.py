voters = ['lissa', 'michael', 'max', 'igor', 'henry', 'sam']

language_pool = {'igor': 'rust',
                 'henry': 'python',
                 'michael': 'C++',
                  }

for name in voters:
    if name in language_pool.keys():
        print(f"Thank you {name.title()} for participating in pool and voting for {language_pool[name].title()} ")
    elif name not in language_pool.keys():
        print(name.title() + " Please take a pool!")
    