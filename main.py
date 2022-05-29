import hashlib

def hashGenerator(data):
    value=hashlib.sha256(data.encode())
    return value.hexdigest()

class Block:
    def __init__(self,Data,hash,prevHash):
        self.Data=Data
        self.hash=hash
        self.prevHash=prevHash

class Blockchain:
    def __init__(self):
      hashLast=hashGenerator('gen_last')
      hashStart=hashGenerator('gen_hash')

      genesis=Block('gen-data',hashStart,hashLast)
      self.chain=[genesis]

    def add_block(self,data):
        prev_hash=self.chain[-1].hash
        hash=hashGenerator(data)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)

bc=Blockchain()
bc.add_block('0')
bc.add_block('1')
bc.add_block('2')

for block in bc.chain:
    print(block.__dict__)

