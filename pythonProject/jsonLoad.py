import json

json_dict = { 'category': 'food', 'name': 'mcdonalds', 'price': '1000' }
json_dict = json.loads(json.dumps(json_dict))
print (json_dict)

# {u'category': u'food', u'price': u'1000', u'name': u'mcdonalds'}
