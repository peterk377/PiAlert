from database import newAlert
from database import login

userID = ''
email = ''
username = ''
password = ''
string = ''
print("Please enter your username.")
username = input()
print("Please enter your password.")
password = input()

userID, email = login(username, password)
print(userID )

while string != 'stop':
    newAlert(userID, email)
    print("press ENTER to create a new alert or write stop to end test")
    string = input()