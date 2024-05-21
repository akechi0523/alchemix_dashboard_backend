import json
from web3 import Web3
from .abi.abi_amo import amo_abi
from .abi.abi_amo_threepool import abi_amo_threepool

# Fill in your infura API key here
mainnet_API_key = "https://mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
arbitrum_API_key = "https://arbitrum-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
optimism_API_key = "https://optimism-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"

web3_mainnet = Web3(Web3.HTTPProvider(mainnet_API_key))
web3_arbitrum = Web3(Web3.HTTPProvider(arbitrum_API_key))
web3_optimism = Web3(Web3.HTTPProvider(optimism_API_key))

AMOs = {
    'alUSD':'0x9735F7d3Ea56b454b24fFD74C58E9bD85cfaD31B',
    'alUSDFRAXBP':'0x06378717d86B8cd2DBa58c87383dA1EDA92d3495',
    'alETH/fraxETH':'0x9fb54d1F6F506Feb4c65B721bE931e59BB538c63'
}

#Function to get AMOs
def getAMO(AMOs, web3):
    AMO = {}
    for address in AMOs.values():
        if address=='0x9735F7d3Ea56b454b24fFD74C58E9bD85cfaD31B':
            contract = web3.eth.contract(address=address, abi=abi_amo_threepool)
            AMO[address] = {
            'admin':contract.functions.admin().call(),
            'AMO':address,
            'twoPool':contract.functions.threePool().call(),
            'convexPoolId':contract.functions.convexPoolId().call(),
            'rewardReceiver':contract.functions.rewardReceiver().call()
        }
        else:
            contract = web3.eth.contract(address=address, abi=amo_abi)
            AMO[address] = {
            'admin':contract.functions.admin().call(),
            'AMO':address,
            'twoPool':contract.functions.twoPool().call(),
            'convexPoolId':contract.functions.convexPoolId().call(),
            'rewardReceiver':contract.functions.rewardReceiver().call()
        }
    return AMO

#Function to convert values to string
def convert_values_to_string(data):
    for key, value in data.items():
        for k, v in value.items():
            if isinstance(v, (int, float, bool)):
                data[key][k] = str(v)
    return data

def fetch_AMO():
    amo = convert_values_to_string(getAMO(AMOs, web3_mainnet))
    return amo

# print(getAMO(AMOs, web3_mainnet))
# with open('AMO.json', 'w') as json_file:
#     json.dump(convert_values_to_string(getAMO(AMOs, web3_mainnet)), json_file)