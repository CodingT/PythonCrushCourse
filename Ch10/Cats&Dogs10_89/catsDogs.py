files = ['cats.txt', 'daogs.txt']

for file in files:
    try:
        with open(file) as file:
            pat_cnames = file.read()
       
    except FileNotFoundError as not_found:
        #pass
        print(f"Pls check file {not_found.filename} is exist")
    else:
        print(f"{pat_cnames}")
   
        