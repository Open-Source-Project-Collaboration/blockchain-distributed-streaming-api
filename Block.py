from hashlib import sha256
import json
import time

class Block:
    def __init__(self, index, transactions, timestamp, prev_hash):
        self.index = index
        self.transactions = transactions
        self.prev_hash = prev_hash
    def compute_hash(self):
        block = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block.encode()).hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = []
        self.create_block()
    def create_block(self):
        blocks = Block(0,[],time.time(), "0")
        blocks.hash = blocks.compute_hash()
        self.chain.append(blocks)
    def get_last_block(self):
        return self.chain[-1]