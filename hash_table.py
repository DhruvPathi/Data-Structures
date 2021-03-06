
class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]
    
    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h%self.max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

ht = HashTable()
ht['march 6'] = 130
print(ht['march 6'])
     