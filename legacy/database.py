def newAlert(userID, email, whatsapp, filename):

    from notification import sendEmail
    from notification import sendWhatsApp
    import pymongo
    from datetime import datetime
    import os
    from dotenv import main
    from encode import encode

    main.load_dotenv()

    whatsapp = whatsapp

    url = os.getenv('DATABASE_URL')
    myclient = pymongo.MongoClient(url)
    db = myclient["pialert"]

    alerts_collection = db["alerts"]

    num = 0


    date = datetime.today().strftime('%d/%m/%Y/ %X') # setting the date to todays date
    for x in alerts_collection.find(): #checking how many alerts are in the database already
        num = num + 1 # assing 1 to total alerts

    alertID = 'a' + str('{:0>6}'.format(num + 1)) # assigning the correct format to alertID eg. a12345

    video = encode(filename)

    query = { "alertID": alertID, "date": "29/04/2024/ 15:44:59", "video": video, "userID":userID } # wrting queries for the database
    

    alerts_collection.insert_one(query) # Updating database with the new alert entry

    


    print('new alert created')

#===================================================================================================================

def login(username, password, whatsapp) :

    import os
    import pymongo
    from dotenv import main
    
    main.load_dotenv()


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
    print("got here")
    return userID, email, whatsapp

#===============================================================================================================