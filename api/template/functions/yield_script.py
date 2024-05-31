import json
from web3 import Web3
from .abi.abi_alchemistv2 import alchemistv2_abi
from .abi.abi_common import common_abi

# Fill in your infura API key here
mainnet_API_key = "https://mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
arbitrum_API_key = "https://arbitrum-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
optimism_API_key = "https://optimism-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"

web3_mainnet = Web3(Web3.HTTPProvider(mainnet_API_key))
web3_arbitrum = Web3(Web3.HTTPProvider(arbitrum_API_key))
web3_optimism = Web3(Web3.HTTPProvider(optimism_API_key))

#Alchemist addresses
mainnet = {
    'alUSD':'0x5C6374a2ac4EBC38DeA0Fc1F8716e5Ea1AdD94dd',
    'alETH':'0x062Bf725dC4cDF947aa79Ca2aaCCD4F385b13b5c'
}
optimism = {
    'alUSD':'0x10294d57A419C8eb78C648372c5bAA27fD1484af',
    'alETH':'0xe04Bb5B4de60FA2fBa69a93adE13A8B3B569d5B4',
}
arbitrum = {
    'alUSD':'0xb46eE2E4165F629b4aBCE04B7Eb4237f951AC66F',
    'alETH':'0x654e16a0b161b150F5d1C8a5ba6E7A7B7760703A',
}

#Function to get yield token
def getYieldToken(alchemist, web3):
    yieldToken = {}
    yieldTokenAddress = []
    yieldTokenParas = []
    if alchemist==mainnet:
        chainName = "Mainnet"
    if alchemist==arbitrum:
        chainName = "Arbitrum"
    if alchemist==optimism:
        chainName = "Optimism"
    for key in alchemist.keys():
        address = alchemist[key]
        contract = web3.eth.contract(address=address, abi=alchemistv2_abi)
        yieldTokenAddress = contract.functions.getSupportedYieldTokens().call()
        for i in yieldTokenAddress:
            yieldTokenParas = contract.functions.getYieldTokenParameters(i).call()
            yieldTokenName = getYieldTokenName(i, web3)
            underlyingTokenPara = contract.functions.getUnderlyingTokenParameters(yieldTokenParas[1]).call()
            yieldToken[i] = {
                'chain':chainName,
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
                'lastDistributionBlock': str(yieldTokenParas[12]),
                'accruedWeight': yieldTokenParas[13],
                'enabled': str(yieldTokenParas[14]),
                'underlyingTokenDecimal': underlyingTokenPara[0]
            }
    return yieldToken

#Function to get yield token name
def getYieldTokenName(yieldTokenAddress, web3):
    contract = web3.eth.contract(address=yieldTokenAddress, abi=common_abi)
    yieldTokenName = contract.functions.name().call()
    return yieldTokenName

def fetch_yieldToken():
    yieldTokens = {
        'mainnet':getYieldToken(mainnet, web3_mainnet),
        'arbitrum':getYieldToken(arbitrum, web3_arbitrum),
        'optimism':getYieldToken(optimism, web3_optimism)
    }
    # with open('1yield.json', 'w') as json_file:
    #     json.dump(yieldTokens, json_file)
    return yieldTokens
