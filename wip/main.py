import json
import os
from jq_requests import jq_get

base_url = 'https://pokeapi.co/api/v2'

result_dict = jq_get(base_url)
r = result_dict['json']


oput = {}

for k, v in r.items():

    res = jq_get(v)
    jres = res['json']

    oput[k]=jres

dump = json.dumps(oput, indent=2)
f = open('log.json', "a")
f.write(dump)
f.close

