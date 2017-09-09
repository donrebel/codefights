class HashTable():
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def get_val(self):
        return None

    def put(self, key, value):
        hash_val = self.hash_function(key)
        if self.slots[hash_val] is None:
            self.slots[hash_val] = key
            self.data[hash_val] = value
        else:
            if self.slots[hash_val] == key:
                self.data[hash_val] = value
            else:
                nextslot = self.rehash_function(hash_val)
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash_function(nextslot)
                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = value
                else:
                    self.data[nextslot] = value

    def get(self, key):
        start_pos = self.hash_function(key)
        data = None
        stop = False
        found = False
        position = start_pos
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash_function(position)
                if self.slots[position] == start_pos:
                    stop = True
        return data

    def is_empty(self):
        return self.slots == []

    def hash_function(self, value):
        return value % self.size

    def rehash_function(self, old_hash):
        return (old_hash + 1) % self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

if __name__ == '__main__':
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"

    print(H.slots)
    print(H.data)
    H[20] = 'duck'
    print(H[20])
    print(H.data)
    print(H[90])