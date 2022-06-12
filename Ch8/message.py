
from xml.dom.minidom import Element


def show_messages(messages):
    """Modifying passed List"""
    print("\n Messages in line to send:")
    for message in messages:
        print(message)


def send_messages(messages):
    """Print and move message to other list"""
    sent_messages = []
    
    print("\n Sending messages:")
    while messages:
        current_message = messages.pop()
        print(current_message + " was sent succesfully")
        sent_messages.append(current_message)
    return sent_messages
        

messages = ['Hola amigos!', 'Sangre por sangre.', 'Viva la Mexico!']

show_messages(messages)

sent_messages = send_messages(messages)
print(f"\n Processed: {sent_messages}")

print(f"\n Messages in queue =  {str(len(messages))} {str(messages)}" )




