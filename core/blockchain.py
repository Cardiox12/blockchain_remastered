from block import Block
from hashlib import sha256
from itertools import zip_longest

class Blockchain():
    def __init__(self):
        self.blocks = []
        self.root_hash = ""

    def add_to_blockchain(self, data):
        """
            This method add a block to the blockchain.
            :param  data: The data to include in the block. 
            :type   data: str
            :returns:   None
            :rtype:     None
        """
        if len(self.blocks) < 1:
            self.blocks.append(Block(data))
        else:
            if all(block.block_is_valid() for block in self.blocks):
                self.blocks.append(Block(data, self.blocks[-1].hash))
        self.blockchain_is_not_corrupted()
    
    def blockchain_is_not_corrupted(self):
        """
            An implementation of the merkle tree that compute hash of all blocks of the blockchain,
            if everybody has the same root_hash computed by the merkle tree, the blockchain is valid,
            otherwise it means that blockchain has been corrupted.
            The root hash computed by the merkle tree update the root hash after every adding in blockchain.

            :returns:   The root hash
            :rtype:     str
        """
        even = [block.hash for i, block in enumerate(self.blocks) if i % 2 == 0]
        odd = [block.hash for i, block in enumerate(self.blocks) if i % 2 != 0]
        temp = []
        if len(self.blocks) > 1:
            while (len(even) > 0 and len(odd) > 0):
                temp = []
                for first, sec in zip_longest(even, odd, fillvalue=""):
                    hasher = sha256()
                    tmp_hash = hasher.update(first.encode() + sec.encode())
                    temp.append(hasher.hexdigest())
                even = [block for i, block in enumerate(temp) if i % 2 == 0]
                odd = [block for i, block in enumerate(temp) if i % 2 != 0]
            self.root_hash = temp[0]
        else:
            self.root_hash = self.blocks[0].hash
        return self.root_hash