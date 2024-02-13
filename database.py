def newAlert(userID):


    import pymongo
    from datetime import datetime

    url = 'mongodb+srv://pete:rkJra6htx7zbBKkH@cluster0.udwnlkv.mongodb.net/?retryWrties=true&w=majority'
    myclient = pymongo.MongoClient(url)
    db = myclient["pialert"]

    alerts_collection = db["alerts"]
    user_collection = db["user"]
    user_has_alerts_collection = db["user_has_alerts"]

    num = 0

    date = datetime.today().strftime('%d/%m/%Y')
    for x in alerts_collection.find():
        num = num + 1

    alertID = 'a' + str('{:0>6}'.format(num + 1))

    print(alertID + " " + date)

    query = { "alertID": alertID, "date": date, "video":"test", "image":"test" }
    query2 = {"userID": userID, "alertID": alertID}

    alerts_collection.insert_one(query)

    user_has_alerts_collection.insert_one(query2)

#===================================================================================================================

def login(username, password) :

    import pymongo

    url = 'mongodb+srv://pete:rkJra6htx7zbBKkH@cluster0.udwnlkv.mongodb.net/?retryWrties=true&w=majority'
    myclient = pymongo.MongoClient(url)
    db = myclient["pialert"]

    user_collection = db["user"]

    query = {"username": username, "password":password}

    x = user_collection.find(query)

    for result in x:
        userID = result['userID']

    return userID

#===============================================================================================================