def newAlert(userID, email, whatsapp):

    from notification import sendEmail
    from notification import sendWhatsApp
    import pymongo
    from datetime import datetime
    import os
    from dotenv import load_dotenv
    from encode import encode

    load_dotenv()

    url = os.getenv('DATABASE_URL')
    myclient = pymongo.MongoClient(url)
    db = myclient["pialert"]

    alerts_collection = db["alerts"]
    user_collection = db["user"]
    user_has_alerts_collection = db["user_has_alerts"]

    num = 0

    video = encode() # encode the video and store in varaible (Currently Testing video are store in the local)

    date = datetime.today().strftime('%d/%m/%Y/ %X') # setting the date to todays date
    for x in alerts_collection.find(): #checking how many alerts are in the database already
        num = num + 1 # assing 1 to total alerts

    alertID = 'a' + str('{:0>6}'.format(num + 1)) # assigning the correct format to alertID eg. a12345

    # print(alertID + " " + date) making sure the data is correct

    query = { "alertID": alertID, "date": date, "video":video, "image":"test" } # wrting queries for the database
    query2 = {"userID": userID, "alertID": alertID}

    alerts_collection.insert_one(query) # Updating database with the new alert entry

    user_has_alerts_collection.insert_one(query2) # Updating the database with the new entry

    #sendEmail(email, "clip.mp4") # Sending a notification email to logged in user
    sendWhatsApp(whatsapp) #Sending notification through whatsapp

#===================================================================================================================

def login(username, password, whatsapp) :

    import os
    import pymongo
    from dotenv import load_dotenv

    load_dotenv()


    url = os.getenv('DATABASE_URL')
    myclient = pymongo.MongoClient(url)
    db = myclient["pialert"]

    user_collection = db["user"]

    query = {"username": username, "password":password}

    x = user_collection.find(query)

    for result in x:
        userID = result['userID']
        email = result['email']
        whatsapp = result['whatsapp']

    return userID, email, whatsapp

#===============================================================================================================