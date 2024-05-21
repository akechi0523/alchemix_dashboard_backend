import json
from web3 import Web3
from abi_transmuter import transmuter_abi
from abi_transmuterbuffer import transmuterbuffer_abi
from abi_common import common_abi

# Fill in your infura API key here
mainnet_API_key = "https://mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
arbitrum_API_key = "https://arbitrum-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
optimism_API_key = "https://optimism-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"

web3_mainnet = Web3(Web3.HTTPProvider(mainnet_API_key))
web3_arbitrum = Web3(Web3.HTTPProvider(arbitrum_API_key))
web3_optimism = Web3(Web3.HTTPProvider(optimism_API_key))

#Transfer addresses
mainnet = {
    'DAI':'0xA840C73a004026710471F727252a9a2800a5197F',
    'USDC':'0x49930AD9eBbbc0EB120CCF1a318c3aE5Bb24Df55',
    'USDT':'0xfC30820ba6d045b95D13a5B8dF4fB0E6B5bdF5b9',
    'FRAX':'0xE107Fa35D775C77924926C0292a9ec1FC14262b2',
    'WETH':'0x03323143a5f0D0679026C2a9fB6b0391e4D64811'
}
optimism = {
    'DAI':'0xFCD619923456E20EAe298B35E3606277b391BBB4',
    'USDC':'0xA7ea9ef9E2b5e15971040230F5d6b75C68Aab723',
    'USDT':'0x4e7d2115E4FeEcD802c96E77B8e03D98104415fa',
    'ETH':'0xb7C4250f83289ff3Ea9f21f01AAd0b02fb19491a'
}
arbitrum = {
    'DAI':'0xD6a5577c2f6200591Fe077E45861B24AeeB408e9',
    'USDC':'0xe7ec71B894583E9C1b07873fA86A7e81f3940eA8',
    'USDT':'0x2a8B5F365Fb29C3E1a40a5cd14AD7f89050755Ed',
    'ETH':'0x1EB7D78d7f6D73e5de67Fa62Fd8b55c54Aa9c0D4'
}

#Function to get transmuter
def getTransmuter(transmuterAddress, web3):
    transmuter = {}
    for address in transmuterAddress.values():
        contract = web3.eth.contract(address=address, abi=transmuter_abi)
        syntheticTokenAddress = contract.functions.syntheticToken().call()
        bufferAddress = contract.functions.buffer().call()
        # print(admin)
        transmuter[address] = {
            'transmuterAddress':address,
            'ADMIN':'0xdf8b4c520ffe197c5343c6f5aec59570151ef9a492f2c624fd45ddde6135ec42',
            'buffer':getBuffer(bufferAddress, web3),
            'syntheticToken':getSyntheticToken(syntheticTokenAddress, web3)
        }
    # print(bufferAddresses)
    return transmuter

#Function to get synthetic token name
def getSyntheticToken(syntheticTokenAddress, web3):
    syntheticToken = {}
    contract = web3.eth.contract(address=syntheticTokenAddress, abi=common_abi)
    syntheticTokenName = contract.functions.name().call()
    syntheticToken[syntheticTokenAddress] = {
        'syntheticTokenAddress':syntheticTokenAddress,
        'name':syntheticTokenName
    }
    return syntheticToken

#Funtion to get buffer
def getBuffer(bufferAddress, web3):
    contract = web3.eth.contract(address=bufferAddress, abi=transmuterbuffer_abi)
    buffer = {}
    underlyingTokenAddress = []
    index = 0
    if bufferAddress=='0x1EEd2DbeB9fc23Ab483F447F38F289cA15f79Bac':#mainnet_alUSD
        i=4
    if bufferAddress=='0xbc2FB245594a68c927C930FBE2d00680A8C90B9e':#mainnet_alETH
        i=2
    if bufferAddress=='0x00E33722ba54545667E76a18CE9D544130eEAbcC':#arbitrum_alUSD
        i=3
    if bufferAddress=='0xECAd08EE07f1AA87f3E080997eBa6d02d28bb9D2':#arbitrum_alETH
        i=1
    if bufferAddress=='0xe99a9A717c60F9639B235ede422c27d60FBEB3b9':#optimism_alUSD
        i=3
    if bufferAddress=='0x7f50923EE8E2BC3596a63998495baf2948a28f68':#optimism_alETH
        i=1

    while index<i:
        address = contract.functions.registeredUnderlyings(index).call()
        index +=1
        underlyingTokenAddress.append(address)

    buffer[bufferAddress] = {
        'bufferAddress':bufferAddress,
        'ADMIN':'0xdf8b4c520ffe197c5343c6f5aec59570151ef9a492f2c624fd45ddde6135ec42',
        'KEEPER':'0x71a9859d7dd21b24504a6f306077ffc2d510b4d4b61128e931fe937441ad1836',
        'alchemist':contract.functions.alchemist().call(),
        'debtToken':contract.functions.debtToken().call(),
        'underlyingTokens':getUnderlyingToken(bufferAddress, underlyingTokenAddress, web3),

    }
    return buffer

#Function to get underlying token
def getUnderlyingToken(bufferAddress, underlyingTokenAddress, web3):
    underlyingToken = {}
    for address in underlyingTokenAddress:
        contract = web3.eth.contract(address=bufferAddress, abi=transmuterbuffer_abi)
        underlyingToken[address] = {
            'underlyingTokenAddress':address,
            'AMOs':contract.functions.amos(address).call(),
            'divertToAMO':contract.functions.divertToAmo(address).call(),
            'flowAvailable':contract.functions.flowAvailable(address).call(),
            'flowRate':contract.functions.flowRate(address).call(),
            'getAvailableFlow':contract.functions.getAvailableFlow(address).call(),
            'lastFlowrateUpdate':contract.functions.lastFlowrateUpdate(address).call(),
            'transmuter':contract.functions.transmuter(address).call()
        }
    return underlyingToken

#Function to convert values to string
def convert_values_to_string(data):
    for key, value in data.items():
        if isinstance(value, dict):
            convert_values_to_string(value)
        elif isinstance(value, list):
            for i in range(len(value)):
                if isinstance(value[i], (int, float, bool)):
                    value[i] = str(value[i])
        elif not isinstance(value, str):
            data[key] = str(value)
    
    return data

def fetch_transmuter():
    transmuter = {
        'mainnet':convert_values_to_string(getTransmuter(mainnet, web3_mainnet)),
        'arbitrum':convert_values_to_string(getTransmuter(arbitrum, web3_arbitrum)),
        'optimism':convert_values_to_string(getTransmuter(optimism, web3_optimism))
    }
    return transmuter

# print(">>>>>>>>>>>>>Mainnet<<<<<<<<<<<<<<<<")
# print(getTransmuter(mainnet, web3_mainnet))
# print(">>>>>>>>>>>>>Arbitrum<<<<<<<<<<<<<<<<")
# print(getTransmuter(arbitrum, web3_arbitrum))
# print(">>>>>>>>>>>>>Optimism<<<<<<<<<<<<<<<<")
# print(getTransmuter(optimism, web3_optimism))

# with open('transmuter_mainnet.json', 'w') as json_file:
#     json.dump(convert_values_to_string(getTransmuter(mainnet, web3_mainnet)), json_file)
# with open('transmuter_arbitrum.json', 'w') as json_file:
#     json.dump(convert_values_to_string(getTransmuter(arbitrum, web3_arbitrum)), json_file)
# with open('transmuter_optimism.json', 'w') as json_file:
#     json.dump(convert_values_to_string(getTransmuter(optimism, web3_optimism)), json_file)


