from web3 import Web3
import json
from datetime import date

noMatched_IMEI="17356"
matched_IMEI="32486873264"
ganache_url="http://127.0.0.1:7545"
web3= Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAddress=web3.eth.accounts[0]
from_address= str(web3.eth.defaultAddress)

print("The type of from_address :",type(from_address))
compiled_contract_path="build/contracts/AuthenticationUser.json"

# when you change something in the contract, you have to truffle migrate it 
#and update the contract_address with the deployed HelloWorld's contract address ( fetched from running 'truffle migrate' command)
# before changing it to contract_address, need to check if the project is synced with ganache or not
# also, check the ganache UI contract , wether the contract has been deployed or not .
 
contract_address=web3.toChecksumAddress("0x94B91d56c8E47BEB0470D8765A955d33423Ef9c9")

with open(compiled_contract_path) as file:
    contract_json=json.load(file)
    contract_abi=contract_json['abi']


contract=web3.eth.contract(address=contract_address,abi=contract_abi)
account_name = contract.functions.compareIMEI(noMatched_IMEI).call()

# message2=contract.functions.getUserById(1).call()
print("User loggedin :",account_name)

today = date.today()
event_date = today.strftime("%B %d,%Y")

# print("Matched!")
print("Date :", event_date)

tx_hash = contract.functions.compareIMEI(noMatched_IMEI).transact({'from':from_address})
tx_receipt=web3.eth.waitForTransactionReceipt(tx_hash)
print('tx_hash: {}'.format(tx_hash.hex()))
block=web3.eth.getBlock('latest')
# print("Latest Block: ",block)

# print("type of block: ",type(block))
to_string_object=web3.toJSON(block)
to_json_object=json.loads(to_string_object)

# print("type of to_json_object: ",type(to_json_object))
print("\n\nlatest block: ",to_json_object)

# if message==True :
#     print("Matched!")
#     print("Date :", event_date)
#     entry_name=contract.functions.getUserNameById
#     tx_hash = contract.functions.compareIMEI(noMatched_IMEI).transact({'from':from_address})
#     tx_receipt=web3.eth.waitForTransactionReceipt(tx_hash)
#     print('tx_hash: {}'.format(tx_hash.hex()))
#     block=web3.eth.getBlock('latest')
#     # print("Latest Block: ",block)

#     print("type of block: ",type(block))
#     to_string_object=web3.toJSON(block)
#     to_json_object=json.loads(to_string_object)

#     print("type of to_json_object: ",type(to_json_object))
#     print("\n\nlatest block: ",to_json_object)
    
    
#     # print("Latest Block: ",block['number','hash','transaction','timestamp','gasLimit','gasUsed'])

#     print("default address: " ,web3.eth.defaultAddress)

# else:
#     print("Not matched!")
#     tx_hash = contract.functions.compareIMEI(noMatched_IMEI).transact({'from':from_address})
#     tx_receipt=web3.eth.waitForTransactionReceipt(tx_hash)
#     print('tx_hash: {}'.format(tx_hash.hex()))
#     block=web3.eth.getBlock('latest')
#     # print("Latest Block: ",block)

#     to_string_object=web3.toJSON(block)
#     to_json_object=json.loads(to_string_object)
#     print("type of to_json_object: ",type(to_json_object))
#     print("\n\nlatest block: ",to_json_object)



