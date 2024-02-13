from database import newAlert
from database import login

userID = ''
username = ''
password = ''
string = ''
print("Please enter your username.")
username = input()
print("Please enter your password.")
password = input()

userID = login(username, password)
print(userID )

while string != 'stop':
    newAlert(userID)
    print("press ENTER to create a new alert or write stop to end test")
    string = input()