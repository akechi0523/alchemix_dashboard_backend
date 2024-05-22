import json
from .functions.yield_script import fetch_yieldToken
from .functions.whitelist_script import fetch_whitelist
from .functions.transmuter_script import fetch_transmuter
from .functions.amo_script import fetch_AMO
from .functions.alchemist_script import fetch_alchemist

def fetch_data():
    data = {
        'yieldTokens':fetch_yieldToken(),
        'alchemist':fetch_alchemist(),
        'whitelist':fetch_whitelist(),
        'amo':fetch_AMO(),
        'transmuter':fetch_transmuter()
    }
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)
    return data
