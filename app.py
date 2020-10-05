from web3 import Web3
import json



fetched_IMEI="123456"
ganache_url="http://127.0.0.1:7545"
web3= Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAddress=web3.eth.accounts[0]
compiled_contract_path="build/contracts/HelloWorld.json"

# when you change something in the contract, you have to truffle migrate it 
#and update the contract_address with the deployed HelloWorld's contract address ( fetched from running 'truffle migrate' command)
# before changing it to contract_address, need to check if the project is synced with ganache or not
# also, check the ganache UI contract , wether the contract has been deployed or not .
 
contract_address=web3.toChecksumAddress("0x3EeeA8e91af305dbee683Ed3222Be3bdD2A451e4")

with open(compiled_contract_path) as file:
    contract_json=json.load(file)
    contract_abi=contract_json['abi']


contract=web3.eth.contract(address=contract_address,abi=contract_abi)
message = contract.functions.compareIMEI(fetched_IMEI).call()

# tx_hash=contract.functions.setPayload('hello').transact()

if message==True :
    tx_hash = contract.functions.compareIMEI(fetched_IMEI).transact({'from':'0x6DA145eFEeBD1725D99bd47f7FE036a42E9521e7'})
    tx_receipt=web3.eth.waitForTransactionReceipt(tx_hash)
    print('tx_hash: {}'.format(tx_hash.hex()))

    block=web3.eth.getBlock('latest')
    print("Latest Block: ",block)

    print("default address: " ,web3.eth.defaultAddress)

else:
    print("Not matched!")
    block=web3.eth.getBlock('latest')
    print("Latest Block: ",block)



