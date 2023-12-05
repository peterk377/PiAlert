from pymongo import MongoClient

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://pete:juayWAfxAjS2VCB0@cluster0.udwnlkv.mongodb.net/?retryWrties=true&w=majority"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    # Create the database for our example (we will use the same database throughout the tutorial
    return client['alerts']

def test_database_connection():
    try:
        # Attempt to get the database
        dbname = get_database()
        print("Connected to the database successfully!")
    except Exception as e:
        print(f"Failed to connect to the database. Error: {e}")

def read_data_from_collection():
    try:
        # Get the database
        dbname = get_database()

        # Choose a collection from the database
        collection_name = 'alerts'  # Replace with the actual collection name
        collection = dbname[collection_name]

        # Query the collection (example: find all documents)
        result = collection.find({})

        # Print the documents
        for document in result:
            print(document)
    except Exception as e:
        print(f"Failed to read data from the database. Error: {e}")

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Run the test
    test_database_connection()