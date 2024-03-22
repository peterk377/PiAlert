from database import newAlert
from database import login

userID = ''
email = ''
username = ''
password = ''
string = ''
whatsapp = ''
print("Please enter your username.")
username = input()
print("Please enter your password.")
password = input()

userID, email, whatsapp = login(username, password, whatsapp)
print(userID)
print(whatsapp)

while string != 'stop':
    newAlert(userID, email, whatsapp)
    print("press ENTER to create a new alert or write stop to end test")
    string = input()