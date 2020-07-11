class Dynamic_linear_hash_table:
    def __init__(self, count):
        self.name = None
        self.count = count
        self.initCapacity = count
        self.array = [None]*count
        self.valuearray = []
        self.maxLoadFactor = 0.75

# Accessors

    def size(self):
        return self.count

    def empty(self):
        if (self.count == 0):
            return False
        else:
            return True

    def capacity(self):
        return (self.array.count(None))

    def member(self, val):
        if val in self.array:
            return True
        return False

    def load_factor(self):
        currcapacity = self.capacity()
        capacity = self.size()
        return ((capacity-currcapacity)/capacity)

    def bin(self, index):
        return (self.array[index])
# Mutators

    def insert(self, val):
        self.valuearray.append(val)
        H = self.Cuckoo(val)
        if(self.array[H] != None):
            H = self.Probe(H)

        self.array[H] = val

    def remove(self, val):
        print()

    def clear(self):
        print()

    def Cuckoo(self, val):
        prod = val*53267
        if(prod < 0):
            prod = (prod+(2**31))
        bit = bin(prod)
        bit = bit[:-5]
        prod = int(bit, 2)
        size = self.capacity()
        H = prod % size
        return(H)

    def Probe(self, h):
        while(self.array[h] != None):
            h = h+1
        return h


# Destructor

#    def __del__(self):
 #       print("Deleted")


def main():
    print()
    test = Dynamic_linear_hash_table(16)
    test.insert(100)
    test.insert(100)
    print(test.array)


main()
