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


#Function to get alchemist parameters
def getAlchemist(alchemist, web3):
    alchemistParas = {}
    underlyingTokenAddress = []
    if alchemist==mainnet:
        chainName = "Mainnet"
    if alchemist==arbitrum:
        chainName = "Arbitrum"
    if alchemist==optimism:
        chainName = "Optimism"
    for key in alchemist.keys():
        address = alchemist[key]
        contract = web3.eth.contract(address=address, abi=alchemistv2_abi)
        debtTokenAddress = contract.functions.debtToken().call()
        underlyingTokenAddress = contract.functions.getSupportedUnderlyingTokens().call()
        alchemistParas[address] = {
            'alchemist':key,
            'chain':chainName,
            'admin':contract.functions.admin().call(),
            'debtToken':getDebtToken(debtTokenAddress, web3),
            'underlyingToken':getUnderlyingToken(underlyingTokenAddress, web3, contract),
            'getMintLimitInfo':contract.functions.getMintLimitInfo().call(),
            'minimumCollateralization':contract.functions.minimumCollateralization().call(),
            'protocolFee':contract.functions.protocolFee().call(),
            'protocolFeeReceiver':contract.functions.protocolFeeReceiver().call(),
            'transferAdapter':contract.functions.transferAdapter().call(),
            'transmuter':contract.functions.transmuter().call(),
            'whitelist':contract.functions.whitelist().call()    
        }
    return alchemistParas

#Function to get debt token
def getDebtToken(debtTokenAddress, web3):
    debtToken = {}
    contract = web3.eth.contract(address=debtTokenAddress, abi=common_abi)
    debtToken[debtTokenAddress] = {
        'debtTokenAddress':debtTokenAddress,
        'name':contract.functions.name().call()
    }
    return debtToken

#Function to get underlying token
def getUnderlyingToken(underlyingTokenAddress, web3, alchemist):
    underlyingToken = {}
    for address in underlyingTokenAddress:
        contract = web3.eth.contract(address=address, abi=common_abi)
        underlyingToken[address] = {
            'underlyingTokenAddress':address,
            'name':contract.functions.name().call(),
            'getLiquidationLimitInfo':alchemist.functions.getLiquidationLimitInfo(address).call(),
            'getRepayLimitInfo':alchemist.functions.getRepayLimitInfo(address).call(),
            'getUnderlyingTokenParameters':alchemist.functions.getUnderlyingTokenParameters(address).call(),
        }
    return underlyingToken

def fetch_alchemist():
    transmuter = {
        'mainnet':getAlchemist(mainnet, web3_mainnet),
        'arbitrum':getAlchemist(arbitrum, web3_arbitrum),
        'optimism':getAlchemist(optimism, web3_optimism)
    }
    return transmuter

