import json
from web3 import Web3
from .abi.abi_bridge import bridge_abi

#Fill in your API here
arbitrum_API_key = "https://arbitrum-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
optimism_API_key = "https://optimism-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
metis_API_key = "https://metis-mainnet.blastapi.io/f413149d-7fc9-4a2e-8b7f-11a854bb6486"

web3_arbitrum = Web3(Web3.HTTPProvider(arbitrum_API_key))
web3_optimism = Web3(Web3.HTTPProvider(optimism_API_key))
web3_metis = Web3(Web3.HTTPProvider(metis_API_key))

#Bridge Address
arbitrum_bridge = "0xEE9deC2712cCE65174B561151701Bf54b99C24C8"
optimism_bridge = "0x8f7492DE823025b4CfaAB1D34c58963F2af5DEDA"
metis_bridge = "0x6B142227A277CE62808E0Df93202483547Ec0188"

#Cross-chain Address
Arbitrum = {
    "alUSD":"0xCB8FA9a76b8e203D8C3797bF438d8FB81Ea3326A",
    "alETH":"0x17573150d67d820542EFb24210371545a4868B03"
}
Optimism = {
    "alUSD":"0xCB8FA9a76b8e203D8C3797bF438d8FB81Ea3326A",
    "alETH":"0x3E29D3A9316dAB217754d13b28646B76607c5f04"
}
Metis = {
    "alUSD":"0x303241e2B3b4aeD0bb0F8623e7442368FED8Faf3",
    "alETH":"0x0E17934B9735D479B2388347fAeF0F4e58b9cc06"
}

#Function to get bridges data
def getBridges(crosschain, bridge, web3):
    bridges = {}
    if crosschain == Arbitrum:
        chainName = "Arbitrum"
    if crosschain  == Metis:
        chainName = "Metis"
    if crosschain == Optimism:
        chainName = "Optimism"
    for key in crosschain:
        contract = web3.eth.contract(address=crosschain[key], abi=bridge_abi)
        bridges[crosschain[key]] = {
            'token':key,
            'chain':chainName,
            'address':crosschain[key],
            'bridge':bridge,
            'burningCurrentLimitOf':contract.functions.burningCurrentLimitOf(bridge).call(),
            'burningMaxLimitOf':contract.functions.burningMaxLimitOf(bridge).call(),
            'mintingCurrentLimitOf':contract.functions.mintingCurrentLimitOf(bridge).call(),
            'mintingMaxLimitOf':contract.functions.mintingMaxLimitOf(bridge).call()
        }
    return bridges

# print(getBridges(Arbitrum, arbitrum_bridge, web3_arbitrum))
# print(getBridges(Optimism, optimism_bridge, web3_optimism))
# print(getBridges(Metis, metis_bridge, web3_metis))

def fetch_bridge():
    bridge = {}
    bridge.update(getBridges(Arbitrum, arbitrum_bridge, web3_arbitrum))
    bridge.update(getBridges(Optimism, optimism_bridge, web3_optimism))
    bridge.update(getBridges(Metis, metis_bridge, web3_metis))
    print (bridge)
    return bridge
