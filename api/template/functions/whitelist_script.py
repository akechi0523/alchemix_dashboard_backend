import json
from web3 import Web3
from .abi.abi_alchemistv2 import alchemistv2_abi
from .abi.abi_whitelist import whitelist_abi

# Fill in your infura API key here
mainnet_API_key = "https://mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
arbitrum_API_key = "https://arbitrum-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
optimism_API_key = "https://optimism-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"

web3_mainnet = Web3(Web3.HTTPProvider(mainnet_API_key))
web3_arbitrum = Web3(Web3.HTTPProvider(arbitrum_API_key))
web3_optimism = Web3(Web3.HTTPProvider(optimism_API_key))

#Transfer addresses
mainnet = {
    'Alchemist_alUSD':'0x5C6374a2ac4EBC38DeA0Fc1F8716e5Ea1AdD94dd',
    'Alchemist_alETH':'0x062Bf725dC4cDF947aa79Ca2aaCCD4F385b13b5c'
    # 'Transmuter_DAI':'0xA840C73a004026710471F727252a9a2800a5197F',
    # 'Transmuter_USDC':'0x49930AD9eBbbc0EB120CCF1a318c3aE5Bb24Df55',
    # 'Transmuter_USDT':'0xfC30820ba6d045b95D13a5B8dF4fB0E6B5bdF5b9',
    # 'Transmuter_FRAX':'0xE107Fa35D775C77924926C0292a9ec1FC14262b2',
    # 'Transmuter_WETH':'0x03323143a5f0D0679026C2a9fB6b0391e4D64811'
}
optimism = {
    'Alchemist_alUSD':'0x10294d57A419C8eb78C648372c5bAA27fD1484af',
    'Alchemist_alETH':'0xe04Bb5B4de60FA2fBa69a93adE13A8B3B569d5B4',
    # 'Transmuter_DAI':'0xFCD619923456E20EAe298B35E3606277b391BBB4',
    # 'Transmuter_USDC':'0xA7ea9ef9E2b5e15971040230F5d6b75C68Aab723',
    # 'Transmuter_USDT':'0x4e7d2115E4FeEcD802c96E77B8e03D98104415fa',
    # 'Transmuter_ETH':'0xb7C4250f83289ff3Ea9f21f01AAd0b02fb19491a'
}
arbitrum = {
    'Alchemist_alUSD':'0xb46eE2E4165F629b4aBCE04B7Eb4237f951AC66F',
    'Alchemist_alETH':'0x654e16a0b161b150F5d1C8a5ba6E7A7B7760703A',
    # 'Transmuter_DAI':'0xD6a5577c2f6200591Fe077E45861B24AeeB408e9',
    # 'Transmuter_USDC':'0xe7ec71B894583E9C1b07873fA86A7e81f3940eA8',
    # 'Transmuter_USDT':'0x2a8B5F365Fb29C3E1a40a5cd14AD7f89050755Ed',
    # 'Transmuter_ETH':'0x1EB7D78d7f6D73e5de67Fa62Fd8b55c54Aa9c0D4'
}

#Function to get whitelist
def getWhitelist(alchemist, web3):
    whitelist = {}
    if alchemist==mainnet:
        chainName = "Mainnet"
    if alchemist==arbitrum:
        chainName = "Arbitrum"
    if alchemist==optimism:
        chainName = "Optimism"
    for address in alchemist.values():
        contract = web3.eth.contract(address=address, abi=alchemistv2_abi)
        whitelistAddress = contract.functions.whitelist().call()
        # print(whitelistAddress)
        whitelist[whitelistAddress] = {
            'whitelistAddress':whitelistAddress,
            'chain':chainName,
            'associatedAlchemist':address,
            'whitelisted':getWhitelisted(whitelistAddress, web3)
        }
    return whitelist

#Function to get whitelisted contract
def getWhitelisted(whitelistAddress, web3):
    whitelisted = []
    contract = web3.eth.contract(address=whitelistAddress, abi=whitelist_abi)
    whitelisted = contract.functions.getAddresses().call()
    return whitelisted

#Function to convert values to string
def convert_values_to_string(data):
    for key, value in data.items():
        for k, v in value.items():
            if isinstance(v, (int, float, bool)):
                data[key][k] = str(v)
    return data

def fetch_whitelist():
    whitelist = {
        'mainnet':convert_values_to_string(getWhitelist(mainnet, web3_mainnet)),
        'arbitrum':convert_values_to_string(getWhitelist(arbitrum, web3_arbitrum)),
        'optimism':convert_values_to_string(getWhitelist(optimism, web3_optimism))
    }
    return whitelist

# print(">>>>>>>>>>>>>Mainnet<<<<<<<<<<<<<<<<")
# print(getWhitelist(mainnet, web3_mainnet))
# print(">>>>>>>>>>>>>Arbitrum<<<<<<<<<<<<<<<<")
# print(getWhitelist(arbitrum, web3_arbitrum))
# print(">>>>>>>>>>>>>Optimism<<<<<<<<<<<<<<<<")
# print(getWhitelist(optimism, web3_optimism))

# with open('whitelist_mainnet.json', 'w') as json_file:
#     json.dump(convert_values_to_string(getWhitelist(mainnet, web3_mainnet)), json_file)
# with open('whitelist_arbitrum.json', 'w') as json_file:
#     json.dump(convert_values_to_string(getWhitelist(arbitrum, web3_arbitrum)), json_file)
# with open('whitelist_optimism.json', 'w') as json_file:
#     json.dump(convert_values_to_string(getWhitelist(optimism, web3_optimism)), json_file)