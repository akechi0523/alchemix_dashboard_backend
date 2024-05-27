import json
from web3 import Web3
from abi.abi_alchemistv2 import alchemistv2_abi
from abi.abi_keeper import keeper_abi

# Fill in your infura API key here
mainnet_API_key = "https://mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
arbitrum_API_key = "https://arbitrum-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"
optimism_API_key = "https://optimism-mainnet.infura.io/v3/245a04220b7442de94d1a26862bbbfa6"

web3_mainnet = Web3(Web3.HTTPProvider(mainnet_API_key))
web3_arbitrum = Web3(Web3.HTTPProvider(arbitrum_API_key))
web3_optimism = Web3(Web3.HTTPProvider(optimism_API_key))

#Alchemist addresses
mainnet= ['0x5C6374a2ac4EBC38DeA0Fc1F8716e5Ea1AdD94dd', '0x062Bf725dC4cDF947aa79Ca2aaCCD4F385b13b5c']
arbitrum = ['0xb46eE2E4165F629b4aBCE04B7Eb4237f951AC66F', '0x654e16a0b161b150F5d1C8a5ba6E7A7B7760703A']
optimism = ['0x10294d57A419C8eb78C648372c5bAA27fD1484af', '0xe04Bb5B4de60FA2fBa69a93adE13A8B3B569d5B4']

#Keeper addresses
mainnet_keeper = '0x718660DA0E4333e2F33D9d56A4e002D6263ab333'
arbitrum_keeper = '0x0370ada82F7A9397Ca26eA5c9f13b937513Ef754'
optimism_keeper = '0x4D9C4EaD535CaC13471d5A597fb7510CCEa99772'

#Function to get keepers
def getKeeper(alchemist, keeper, web3):
    keepers = {}
    yieldTokenAddress =[]
    keeperParas = []
    if alchemist == mainnet:
        chainName = "Mainnet"
    if alchemist  == arbitrum:
        chainName = "Arbitrum"
    if alchemist == optimism:
        chainName = "Optimism"
    for address in alchemist:
        contractToGetYieldTokenAddress = web3.eth.contract(address=address, abi=alchemistv2_abi)
        yieldTokenAddress = contractToGetYieldTokenAddress.functions.getSupportedYieldTokens().call()
        for i in yieldTokenAddress:
            contractToGetKeeper = web3.eth.contract(address = keeper, abi = keeper_abi)
            keeperParas = contractToGetKeeper.functions.harvestJobs(i).call()
            keepers[i] = {
                'chain':chainName,
                'active':keeperParas[0],
                'alchemist':keeperParas[1],
                'yeidToken':keeperParas[2],
                'lastHarvest':keeperParas[3],
                'minimumHarvestAmount':keeperParas[4],
                'minimumDelay':keeperParas[5],
                'slippageBps':keeperParas[6]
            }
    return keepers

def fetch_keeper():
    keepers = {
        'mainnet':getKeeper(mainnet, mainnet_keeper, web3_mainnet),
        'arbitrum':getKeeper(arbitrum, arbitrum_keeper, web3_arbitrum),
        'optimism':getKeeper(optimism, optimism_keeper, web3_optimism)
    }
    with open('keepers.json', 'w') as json_file:
        json.dump(keepers, json_file)
    print(keepers)
    return keepers

fetch_keeper()

