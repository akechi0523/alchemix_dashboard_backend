import json
from .functions.yield_script import fetch_yieldToken
from .functions.whitelist_script import fetch_whitelist
from .functions.transmuter_script import fetch_transmuter
from .functions.amo_script import fetch_AMO
from .functions.alchemist_script import fetch_alchemist

data = {
        'yieldTokens':fetch_yieldToken(),
        'alchemist':fetch_alchemist(),
        'whitelist':fetch_whitelist(),
        'amo':fetch_AMO(),
        'transmuter':fetch_transmuter()
    }
# Function to convert large numbers and booleans to readable format
def convert_data(data):
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = convert_data(value)
    elif isinstance(data, list):
        for i in range(len(data)):
            data[i] = convert_data(data[i])
    elif isinstance(data, int) or isinstance(data, float):
        if abs(data) >= 1e6:
            data = f'{data:.3e}'
    return data

# Convert data in the JSON
converted_data = convert_data(data)

def fetch_data():
    with open('data.json', 'w') as json_file:
        json.dump(convert_data, json_file)