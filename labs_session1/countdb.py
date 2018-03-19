from pymongo import MongoClient

mongo_uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)
db = client.get_default_database()

customers = db['customers']

count_by_ref = {
    'ads': 0,
    'wom': 0,
    'events': 0
}

for ref_method in count_by_ref:
    count_by_ref[ref_method] = customers.find({'ref': ref_method}).count()

print(count_by_ref)

#ve piechart
import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot

labels = []
values = []
for key,value in count_by_ref.items():
    labels.append(key)
    values.append(value)

colors = ['yellow','purple','pink']
pyplot.pie(values,labels=labels,colors=colors,shadow=True)
pyplot.axis('equal')
pyplot.show()
