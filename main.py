import json
import shodan
import mongodbsearch
import visualize
import itertools

dbArr = []
collArr = []

filename = 'apikey'
with open(filename, 'r') as f:
    APIKEY = f.read().strip()

print('%s\n' % APIKEY)

api = shodan.Shodan(APIKEY)

query = 'MongoDB Server Information'

try:
    results = api.search(query)

    print('Shodan Summary Information')
    print('Query: %s' % query)
    print('Total Results: %s\n' % results['total'])

    for result in results['matches']:
        if "Authentication partially enabled" not in result['data']:
            print('IP: {}'.format(result['ip_str']))
            ip: str = format(result['ip_str'])
            collections = mongodbsearch.getCollections(ip)
            if collections:
                data = json.loads(collections)
                for dbName, collName in data.items():
                    dbArr.append(dbName)
                    collArr.append(collName)

    dbText = ' '.join(dbArr)
    collText = ' '.join(list(itertools.chain(*collArr)))

    visualize.createWordCloud(dbText)
    visualize.createWordCloud(collText)

except shodan.APIError as e:
    print('Error: {}'.format(e))
