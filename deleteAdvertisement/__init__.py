import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://apollo-udacity-cosmosdb:UdW5syCrPZQXy2L2mCoQMzIGyzIX3RQDTZVOSnxct4Xpg1UDmVmAgEaLvS4INfvSMJwrO3LPMPUPWfuEtpTXdg==@apollo-udacity-cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@apollo-udacity-cosmosdb@"
            client = pymongo.MongoClient(url)
            database = client['neighborly-db']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
