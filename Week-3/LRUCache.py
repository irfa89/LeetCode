"""
146. Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

"""


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = []
        self.lookup = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.lookup:
            return -1

        self.cache.remove(key)
        self.cache.append(key)
        return self.lookup[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.lookup:
            self.lookup[key] = value
            self.cache.remove(key)
            self.cache.append(key)
            return
        else:
            if len(self.cache) == self.capacity:
                delete = self.cache[0]
                self.cache = self.cache[1:]
                del self.lookup[delete]
            self.cache.append(key)
            self.lookup[key] = value

def main():
    lru = LRUCache(2)
    lru.put(1,1)
    lru.put(2,2)
    lru.get(2)
    lru.put(4,4)
    lru.get(3)
    lru.get(3)
    lru.get(4)


if __name__ == "__main__":
    main()