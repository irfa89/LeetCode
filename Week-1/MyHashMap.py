"""
706. Design a HashMap without using any built-in hash table libraries.To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap.If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Leetcode : Running successful but time Limit exceeded.
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 100
        self.opertns = 101
        self.hsh_tbl = [[] for _ in range(0,self.size)]

    def __hash__(self,key):
        return key % self.size

    def __pos__(self,key):
        return key//self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hsh_key = self.__hash__(key)
        if not self.hsh_tbl[hsh_key]:
            self.hsh_tbl[hsh_key] = [None]*self.opertns
        self.hsh_tbl[hsh_key][self.__pos__(key)] = value



    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hsh_key = self.__hash__(key)
        if (not self.hsh_tbl[hsh_key]) or self.hsh_tbl[hsh_key][self.__pos__(key)] == None:
            return -1
        else:
            return self.hsh_tbl[hsh_key][self.__pos__(key)]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hsh_key = self.__hash__(key)
        if self.hsh_tbl[hsh_key]:
            self.hsh_tbl[hsh_key][self.__pos__(key)] = None



def main():
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    print(hashMap.get(1))
    print(hashMap.get(3))
    hashMap.put(2, 1)
    print(hashMap.get(2))
    hashMap.remove(2)
    print(hashMap.get(2))

if __name__ == "__main__":
    main()