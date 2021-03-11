# h(k,i) = (h'(k) + i) mod m
# to do come up with my own hash function
# using pythons hash to compute hash of num
#improve it 
#make while loop which check == None into a different method
#only added number support yet

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.containers = 8
        self.containers_filled = 0
        self.array = [None]* 8
        self.loadFactor = 0.75
        
    def threshold_reached(self):
        return ((self.containers_filled + 1)/self.containers) > self.loadFactor

    def add(self, key: int) -> None:
        
        # hashvalue = hash(key) % self.containers
        
        if not self.contains(key):
        
            if self.threshold_reached():
                self.resize()

            i = 0
            hashvalue = hash(key) % self.containers
            while self.array[hashvalue] != None and self.array[hashvalue] != "deleted":
                i += 1
                hashvalue = (hash(key) + i ) % self.containers
                
            if self.array[hashvalue] != "deleted":
                self.containers_filled += 1
                
            self.array[hashvalue] = key
            

    def remove(self, key: int) -> None:

        i = 0
        hashvalue = (hash(key) + i ) % self.containers

        while self.array[hashvalue] != None:
            if key == self.array[hashvalue]:
                self.array[hashvalue] = "deleted"
                self.containers_filled -= 1
                return
            i += 1
            hashvalue = (hash(key) + i ) % self.containers
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = 0
        hashvalue = (hash(key) + i ) % self.containers
        while self.array[hashvalue] != None:
            if key == self.array[hashvalue]:
                return True
            i += 1
            hashvalue = (hash(key) + i ) % self.containers
        return False

    def resize(self):
        """
        resizing arrays
        """

        self.containers *= 2
        new_array = self.array
        self.array = [None] * self.containers
        self.containers_filled = 0

        for nums in new_array:
            self.add(nums)

        del new_array