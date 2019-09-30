import requests
from requests.auth import HTTPBasicAuth
import json

ENDPOINT="https://gateway-wdc.watsonplatform.net/tone-analyzer/api"
API_KEY="TiOOagJCNlypZNNRn6tMTm1UUR6cCtgVso4tkD8Fw-JB"


def getTones(text:dict, sentence=False): # Dict in format '{"text": "YOUR TEXT"}'
    if len(text['text']) < 20:
        return {'document_tone': {'tones': []}}
    headers={'Content-Type': 'application/json'}
    sent = '&sentences=false' if not sentence else ''
    res = requests.post(url=ENDPOINT+'/v3/tone?version=2017-09-21' + sent, auth=HTTPBasicAuth('apikey', API_KEY), headers=headers, json=text)
    if res.ok:
        data = json.loads(res.content)
        return data
    else:
        return