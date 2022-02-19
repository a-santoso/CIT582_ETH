from web3 import Web3
from hexbytes import HexBytes

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

if w3.isConnected():
#     This line will mess with our autograders, but might be useful when debugging
#    print( "Connected to Ethereum node" )
    pass
else:
    print( "Failed to connect to Ethereum node!" )

def get_transaction(tx):
    tx = w3.eth.get_transaction(tx)
    return tx

# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    gas_price = w3.eth.get_transaction(tx).get('gasPrice')
    return gas_price

def get_gas(tx):
    gas = w3.eth.get_transaction_receipt(tx).get('gasUsed')
    return gas

def get_transaction_cost(tx):
    tx_cost = get_gas_price(tx) * get_gas(tx)
    return tx_cost

def get_block_cost(block_num):
    arrayTxs = w3.eth.getBlock(block_num).get('transactions')

    block_cost = 0

    for tx in arrayTxs:
        block_cost = block_cost + (get_transaction_cost(tx)/1000000000000000000)

#    print("Block cost: ", block_cost)
    return block_cost

# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    arrayTxs = w3.eth.getBlock(block_num).get('transactions')

    maxTrx = 0
    tx_hash = 0

    for tx in arrayTxs:
        tx_cost = get_transaction_cost(tx)/1000000000000000000
        if tx_cost > maxTrx:
            maxTrx = tx_cost
            tx_hash = tx

    print("Hash: ", tx_hash.hex())
    print("Max cost: ", maxTrx)

#    max_tx = HexBytes(tx_hash.hex())
#    print("Hexbytes: ", max_tx)

    max_tx = tx_hash.hex()

    #max_tx = HexBytes('0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6')  #YOUR CODE HERE
    return max_tx


# MAIN!!!

def main():

    print("Q3")
    get_most_expensive_transaction(10237208)

'''
    blockCost = get_block_cost(10237208)
    ethPrice = 248.26
    print("ETH transactions cost: ", blockCost)
    totalCost = blockCost + 2
    print("ETH total cost: ", totalCost)
    print("USD cost: ", ethPrice*totalCost)
    print("USD cost: ", round(ethPrice*totalCost))
'''



'''
    
    print("Q2")
    totalBlockCost = 0;

    for i in range(10237100, 10237110):
        print("Block :", i)
        blockCost = get_block_cost(i)
        totalBlockCost = totalBlockCost + blockCost
        print("Block cost: ",blockCost)

    avgBlockCost = totalBlockCost/(10237110-10237100)
    print("Average block cost: ", avgBlockCost)
'''

'''
    print("Q1")
    tx = "0x0dda1142828634746a8e49e707fddebd487355a172bfa94b906a151062299578"
    print(get_gas(tx))
    print(get_gas_price(tx))

    gwei_cost = get_transaction_cost(tx)
    ETH_price = 1385.02
    dollar_cost = (gwei_cost/1000000000000000000)*ETH_price
    print(dollar_cost)

'''



if __name__ == "__main__":
    main()