import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://apollo-udacity-cosmosdb:UdW5syCrPZQXy2L2mCoQMzIGyzIX3RQDTZVOSnxct4Xpg1UDmVmAgEaLvS4INfvSMJwrO3LPMPUPWfuEtpTXdg==@apollo-udacity-cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@apollo-udacity-cosmosdb@"
        client = pymongo.MongoClient(url)
        database = client['neighborly-db']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)