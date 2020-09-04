import pymongo


# Generic constants
STATUS = 'status'
SUCCESS = 'success'
ERROR = 'error'
DATA = 'data'

#Creating DB

client = pymongo.MongoClient("mongodb+srv://aavishkar_mishra:asdfghjkl@cluster0.9mzve.mongodb.net/?retryWrites=true&w=majority")
mydb = client.test  

#DB FOR IMAGES
