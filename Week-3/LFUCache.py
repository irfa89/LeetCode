"""
460. Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently
used item before inserting a new item. For the purpose of this problem, when there is a tie
(i.e., two or more keys that have the same frequency), the least recently used
key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Soln : Incorrect

"""


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.frequency = {}
        self.cache_index = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        index = self.cache_index[key]
        self.frequency[index].remove(key)
        if self.frequency[index] == []:
            del self.frequency[index]
        if index+1 in self.frequency:
            self.frequency[index+1].append(key)
        else:
            self.frequency[index+1] = [key]
        self.cache_index[key] += 1
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0:
            return
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return
        if len(self.cache) == self.capacity:
            for times in self.frequency:
                key_of_cache = self.frequency[times][0]
                del self.cache[key_of_cache]
                del self.cache_index[key_of_cache]
                self.frequency[times] = self.frequency[times][1:]
                if self.frequency[times] == []:
                    del self.frequency[times]
                    break

        self.cache[key] = value
        if 1 in self.frequency:
            self.frequency[1].append(key)
        else:
            self.frequency[1] = [key]
        self.cache_index[key] = 1

def main():
    lfu = LFUCache(2)
    lfu.put(1,1)
    lfu.put(1, 1)
    lfu.put(2, 2)
    lfu.get(1)
    lfu.put(3, 3)
    lfu.get(2)
    lfu.get(3)
    lfu.put(4, 4)
    lfu.get(1)
    lfu.get(3)
    lfu.get(4)


if __name__ == "__main__":
    main()