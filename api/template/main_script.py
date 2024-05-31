import json
from .functions.yield_script import fetch_yieldToken
from .functions.whitelist_script import fetch_whitelist
from .functions.transmuter_script import fetch_transmuter
from .functions.amo_script import fetch_AMO
from .functions.alchemist_script import fetch_alchemist
from .functions.keeper_script import fetch_keeper
from .functions.bridge_script import fetch_bridge

data = {
        'yieldTokens':fetch_yieldToken(),
        'alchemist':fetch_alchemist(),
        'whitelist':fetch_whitelist(),
        'amo':fetch_AMO(),
        'transmuter':fetch_transmuter(),
        'keeper':fetch_keeper(),
        'bridge':fetch_bridge()
    }
# Function to convert large numbers and booleans to readable format
# def convert_data(data):
#     if isinstance(data, dict):
#         for key, value in data.items():
#             data[key] = convert_data(value)
#     elif isinstance(data, list):
#         for i in range(len(data)):
#             data[i] = convert_data(data[i])
#     elif isinstance(data, int) or isinstance(data, float):
#         if abs(data) >= 1e6:
#             data = f'{data:.3e}'
#     return data

# # Convert data in the JSON
# converted_data = convert_data(data)

# Function to convert boolean values to strings
def convert_booleans_to_strings(data):
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = convert_booleans_to_strings(value)
    elif isinstance(data, list):
        for i in range(len(data)):
            if isinstance(data[i], bool):
                data[i] = str(data[i])
            elif isinstance(data[i], list):
                data[i] = convert_booleans_to_strings(data[i])
    elif isinstance(data, bool):
        data = str(data)
    return data


# Convert boolean values in the JSON data to strings
final_data = convert_booleans_to_strings(data)

def fetch_data():
    with open('data.json', 'w') as json_file:
        json.dump(final_data, json_file)
