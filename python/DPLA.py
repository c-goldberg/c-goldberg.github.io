from dpla.api import DPLA
import os
my_api_key = os.getenv('API_KEY')

dpla_connection = DPLA(my_api_key)

result = dpla_connection.search('austen')
print(type(result))
print(str(result.__dict__)[:1000])
item = result.items[15]

item['sourceResource']['stateLocatedIn']
