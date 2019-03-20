import pymongo
import json


def getCollections(ip):
    try:
        client = pymongo.MongoClient(ip, 27017, maxPoolSize=10)
        c = dict((db, [collection for collection in client[db].list_collection_names()])
                 for db in client.list_database_names())
        return json.dumps(c)
    except:
        print('Error: Cannot retrieve collection list')

def getDBSize(ip):
    try:
        client = pymongo.MongoClient(ip, 27017, maxPoolSize=10)
        for db in client.list_database_names():
            dbstat = client[db].command("dbstats")
            print('DBStat %s\n' % dbstat)
    except:
        print('Error: Cannot retrieve DB Stats')
