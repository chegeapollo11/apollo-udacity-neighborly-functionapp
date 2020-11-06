import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://apollo-udacity-cosmosdb:UdW5syCrPZQXy2L2mCoQMzIGyzIX3RQDTZVOSnxct4Xpg1UDmVmAgEaLvS4INfvSMJwrO3LPMPUPWfuEtpTXdg==@apollo-udacity-cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@apollo-udacity-cosmosdb@"
        client = pymongo.MongoClient(url)
        database = client['azure']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

