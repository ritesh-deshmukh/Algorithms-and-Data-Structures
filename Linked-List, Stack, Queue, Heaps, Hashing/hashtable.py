class HashTable(object):

    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

# Get ASCII value for string type key and % size => to avoid array out of bound error
    def hashfunction(self, key):
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])
        # print(ord(key[pos]))
        return sum % self.size


# Open addressing => linear probing => technique to avoid collision
# Remove collisions
# method 1 => Chaining = using linked-lists
# method 2 => open addressing = generate a new index with the next available slot
    def put(self, key, data): # data => value
        index = self.hashfunction(key)
        # check for collisions
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data
                return
            # rehash try to find another slot
            index = (index+1) % self.size
        # insert
        self.keys[index] = key
        self.values[index] = data

    def get(self, key):
        index = self.hashfunction(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.size
        # if key not found in associative array
        return None


table = HashTable()
table.put("apple", 10)
table.put("orange", 20)
table.put("pear", 30)
table.put("mango", 40)

print(table.get("apple"))
print(table.get("orange"))
print(table.get("pear"))
print(table.get("mango"), "\n")
# print(table.hashfunction("apple"))
# print(table.hashfunction("orange"))
# print(table.hashfunction("pear"))
# print(table.hashfunction("mango"))
