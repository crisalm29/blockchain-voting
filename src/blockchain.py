# blockchain.py


from block import Block

block_chain = [Block.create_genesis_block()]

print("The genesis block has been created")
print("Hash: %s" % block_chain[-1].hash)

