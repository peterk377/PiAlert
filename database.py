def newAlert(userID, email, whatsapp, filename):

    from notification import sendEmail
    from notification import sendWhatsApp
    import pymongo
    from datetime import datetime
    import os
    from dotenv import main
    from encode import encodefile

    main.load_dotenv()

    whatsapp = whatsapp

    url = os.getenv('DATABASE_URL')
    myclient = pymongo.MongoClient(url)
    db = myclient["pialert"]

    alerts_collection = db["alerts"]
    user_collection = db["user"]
    user_has_alerts_collection = db["user_has_alerts"]

    num = 0

    video = encodefile(filename) # encode the video and store in varaible (Currently Testing video are store in the local)

    date = datetime.today().strftime('%d/%m/%Y/ %X') # setting the date to todays date
    for x in alerts_collection.find(): #checking how many alerts are in the database already
        num = num + 1 # assing 1 to total alerts

    alertID = 'a' + str('{:0>6}'.format(num + 1)) # assigning the correct format to alertID eg. a12345

    # print(alertID + " " + date) making sure the data is correct

    query = { "alertID": alertID, "date": date, "video":"testvid", "image":"test", "userID":userID } # wrting queries for the database
    query2 = {"userID": userID, "alertID": alertID}

    alerts_collection.insert_one(query) # Updating database with the new alert entry

    user_has_alerts_collection.insert_one(query2) # Updating the database with the new entry

    sendEmail(email, filename) # Sending a notification email to logged in user
    sendWhatsApp(whatsapp) #Sending notification through whatsapp
    print('new alert created')

#===================================================================================================================

def login(username, password, whatsapp) :

    import os
    import pymongo
    from dotenv import main
    from encode import encodeDetails, decodeDetails

    main.load_dotenv()


    url = os.getenv('DATABASE_URL')
    myclient = pymongo.MongoClient(url)
    db = myclient["pialert"]

    user_collection = db["user"]

    encodedUsername = encodeDetails(username)
    encodedPassword = encodeDetails(password)

    query = {"username": encodedUsername, "password":encodedPassword}

    x = user_collection.find(query)

    userID = ''
    email = ''
    whatsapp = ''

    for result in x:
        userID = result['userID']
        email = result['email']
        whatsapp = result['whatsapp']


    if(userID == ''):
        return "incorrect details","incorrect details","incorrect details",1

    else:
        return userID, decodeDetails(email), decodeDetails(whatsapp),0

#===============================================================================================================