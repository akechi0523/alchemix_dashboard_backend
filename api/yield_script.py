import json
from web3 import Web3
from abi_alchemistv2 import alchemistv2_abi
from abi_common import common_abi

# Fill in your infura API key here
mainnet_API_key = "https://mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
arbitrum_API_key = "https://arbitrum-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
optimism_API_key = "https://optimism-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"

web3_mainnet = Web3(Web3.HTTPProvider(mainnet_API_key))
web3_arbitrum = Web3(Web3.HTTPProvider(arbitrum_API_key))
web3_optimism = Web3(Web3.HTTPProvider(optimism_API_key))

#Alchemist addresses
mainnet = ['0x5C6374a2ac4EBC38DeA0Fc1F8716e5Ea1AdD94dd', '0x062Bf725dC4cDF947aa79Ca2aaCCD4F385b13b5c']
arbitrum = ['0xb46eE2E4165F629b4aBCE04B7Eb4237f951AC66F', '0x654e16a0b161b150F5d1C8a5ba6E7A7B7760703A']
optimism = ['0x10294d57A419C8eb78C648372c5bAA27fD1484af', '0xe04Bb5B4de60FA2fBa69a93adE13A8B3B569d5B4']

#Function to get yield token
def getYieldToken(alchemist, web3):
    yieldToken = {}
    yieldTokenAddress = []
    yieldTokenParas = []
    for address in alchemist:
        contract = web3.eth.contract(address=address, abi=alchemistv2_abi)
        yieldTokenAddress = contract.functions.getSupportedYieldTokens().call()
        for i in yieldTokenAddress:
            yieldTokenParas = contract.functions.getYieldTokenParameters(i).call()
            yieldTokenName = getYieldTokenName(i, web3)
            yieldToken[i] = {
                'Name':yieldTokenName,
                'Decimals':yieldTokenParas[0],
                'underlyingToken': yieldTokenParas[1],
                'adapter': yieldTokenParas[2],
                'maximumLoss': yieldTokenParas[3],
                'maximumExpectedValue': yieldTokenParas[4],
                'creditUnlockRate': yieldTokenParas[5],
                'activeBalance': yieldTokenParas[6],
                'harvestableBalance': yieldTokenParas[7],
                'totalShares': yieldTokenParas[8],
                'expectedValue': yieldTokenParas[9],
                'pendingCredit': yieldTokenParas[10],
                'distributedCredit': yieldTokenParas[11],
                'lastDistributionBlock': yieldTokenParas[12],
                'accruedWeight': yieldTokenParas[13],
                'enabled': yieldTokenParas[14]
            }
    return yieldToken

#Function to get yield token name
def getYieldTokenName(yieldTokenAddress, web3):
    contract = web3.eth.contract(address=yieldTokenAddress, abi=common_abi)
    yieldTokenName = contract.functions.name().call()
    return yieldTokenName

#Function to convert values to string
def convert_values_to_string(data):
    for key, value in data.items():
        for k, v in value.items():
            if isinstance(v, (int, float, bool)):
                data[key][k] = str(v)
    return data

# print(">>>>>>>>>>>>>Mainnet<<<<<<<<<<<<<<<<")
# print(getYieldToken(mainnet, web3_mainnet))
# print(">>>>>>>>>>>>>Arbitrum<<<<<<<<<<<<<<<<")
# print(getYieldToken(arbitrum, web3_arbitrum))
# print(">>>>>>>>>>>>>Optimism<<<<<<<<<<<<<<<<")
# print(getYieldToken(optimism, web3_optimism))
def fetch_yieldToken():
    yieldTokens = {
        'mainnet':convert_values_to_string(getYieldToken(mainnet, web3_mainnet)),
        'arbitrum':convert_values_to_string(getYieldToken(arbitrum, web3_arbitrum)),
        'optimism':convert_values_to_string(getYieldToken(optimism, web3_optimism))
    }
    return yieldTokens

# with open('yield_mainnet.json', 'w') as json_file:
#     json.dump(convert_values_to_string(getYieldToken(mainnet, web3_mainnet)), json_file)
# with open('yield_arbitrum.json', 'w') as json_file:
#     json.dump(convert_values_to_string(getYieldToken(arbitrum, web3_arbitrum)), json_file)
# with open('yield_optimism.json', 'w') as json_file:
#     json.dump(convert_values_to_string(getYieldToken(optimism, web3_optimism)), json_file)