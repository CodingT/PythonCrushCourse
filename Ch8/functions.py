from sqlalchemy import true


def display_message():
    """Displaying message"""
    print("Hello World with functions!")
    
#display_message()

def favorite_book(title):
    """Requied ne parameter"""
    print(f"One of my favorite books is {title.title()}.")

#title = input("Whats is one of your favorite books? \n")
#favorite_book(title)

def make_shirt(size='l', text='We love Python!'):
    """Positional and Key word arguments"""
    print(f"You have ordered {size.upper()} size shirt with '{text}' on it.")
    
#size = input("Whats your shirt size?\n")
#text = input("What would you like to print on the shirt? \n")
#make_shirt(size, text)
#make_shirt(size='xm', text='Im not gay, but $20 is $20 :)')
#make_shirt('l','Hello World!')
#make_shirt()

def describe_city(city, country='usa'):
    """Default parameter value"""
    print(f"{city.title()} is in {country.title()}.")
#describe_city('new york')  describe_city('madrid', 'spain')
#describe_city(country='brazil', city='rio de janeiro')

def city_country(city, country):
    """returning value"""
    output = city.title() +', '+ country.title()
    return output
destination = city_country('new york', 'usa')
#print(destination) 

def make_album(name, title, tracks=''):
    """Making Dictionary in function"""
    album = {'musician':name, 'album_title':title}
    if tracks:
        album['tracks'] = tracks
    return album
#album = make_album('50 cent', 'get rich', '15')
#print(album)
#print("Please enter album info or 'q' to quit:\n")

#while True:
 #   name = input("Artist name is: \n")
 #   if name == 'q':
  #      break
  #  title = input("Album title:\n")
    
#if title == 'q':
    #    break
   # tracks = input("Number of racks in the album:\n")
   # if tracks == 'q':
    #    break
   # album = make_album(name, title, tracks)
    #print(album)
#print("Thanks for responding!")


def show_magicians(magicians):
    """Printing a list """
    for magician in magicians:
        print(f"Please welcome {magician.title()}!")

wizzards = ['david blane', 'harry huddini', 'harry potter']
#show_magicians(wizzards)

def make_great(magicians):
    """Modifying a list"""
    while magicians:
        great_magicians = []
        greating_magician = f"Great {magicians.pop()}"
        great_magicians.append(greating_magician)
        return great_magicians

great_magicians = make_great(wizzards)    
for magician in great_magicians:
    print(f"{magician} \n") 
    


