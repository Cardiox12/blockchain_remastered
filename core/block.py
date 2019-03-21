from datetime import datetime
from hashlib import sha256

class Block():
    block_number = 0

    def __init__(self, data, previous_hash=""):
        Block.block_number += 1
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.timestamp = datetime.now()
        self.hash = self.get_hash()

    def get_hash(self):
        to_digest = "".join([str(item) for item in self.__dict__.values()])
        to_digest += str(Block.block_number)
        hash_ = sha256()
        hash_.update(to_digest.encode())
        self.hash = hash_.hexdigest()
        return self.hash
    
    def mine(self):
        """
            This method hash the block and increment nonce until hash is valid.
            A hash is valid only if the first 4 characters are 0.

            :returns: the valid hash
            :rtype: str
        """
        while not self.block_is_valid():
            self.nonce += 1
            self.get_hash()
        return self.hash

    
    def block_is_valid(self):
        return True if all(num == '0' for num in self.hash[:4]) else False

if __name__ == '__main__':
    block = Block("hello")
    block.get_hash()
    block.mine()
