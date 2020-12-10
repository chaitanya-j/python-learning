import hashlib
class Block:
    def __init__(self,prev_hash,data):
        self.prev_hash = prev_hash
        self.data = data

    def get_hash(self):
        h = hashlib.sha256()
        h.update(bytes(f'{self.prev_hash}','utf-8'))
        h.update(bytes(f'{self.data}','utf-8'))
        return h.hexdigest()

    def __str__(self):
        return f'Block(prev_hash = {self.prev_hash}, Data = {self.data})'

    def __repr__(self):
        return {'prev_hash': f'{self.prev_hash}','Data':f'{self.data}'}