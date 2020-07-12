import random


class Dynamic_linear_hash_table:
    def __init__(self, count):
        self.name = None
        self.count = count
        self.initCapacity = count
        self.currCapacity = count
        self.array = [None]*count

# Accessors

    def size(self, array):
        return len(array)

    def empty(self):
        if (self.count == 0):
            return False
        else:
            return True

    def capacity(self, array):
        return (array.count(None))

    def member(self, val, array):
        size = len(array)
        H = self.value(val, array)
        while(array[H] != None):
            if(array[H] == val):
                return True
        return False

    def load_factor(self, array):
        currcapacity = self.capacity(array)
        capacity = self.size(array)
        lf = ((capacity-currcapacity)/capacity)
        return lf

    def bin(self, index):
        return (self.array[index])
# Mutators

    def insert(self, val):
        # if(not self.member(val)):
        self.array = self.Cuckoo(self.array, val)
        # else:
     #   print("Value already present")

    def doubleSize(self, array):
        newArray = [None]*2*(len(array))
        for element in array:
            if (element != None):
                val = self.value(element)
                size = self.size(newArray)
                H = val % size
                while(newArray[H] != None):
                    H = H+1
                newArray[H] = element
        return(newArray)

    def remove(self, val):
        print()

    def clear(self):
        print()

    def value(self, val, size):
        newVal = val*53267
        if(newVal <= 0):
            newVal = (newVal+(2**31))
        bit = bin(newVal)
        bit = bit[:-5]

        H = int(bit, 2) % size

        return (H)

    def Cuckoo(self, array, val):
        size = self.capacity(array)
        H = self.value(val, size)
        lf = self.load_factor(array)
        if (lf > 0.75):
            array = self.doubleSize(array)
        i = 0
        while(array[(H+i) % size] != None and i < size):
            H = H+1
            if(H == len(array)-1):
                H = 0
            i += 1
        array[H] = val
        print(H, val)
        return(array)
# Destructor

#    def __del__(self):
 #       print("Deleted")


def main():
    print()
    test = Dynamic_linear_hash_table(2**4)
    """
    a = []
    for i in range(0, 16):
        a.append(random.randint(1, 100))
    print(a)
    for element in a:
        test.insert(element)
    """
    test.insert(1)
    test.insert(53)
    test.insert(93)
    test.insert(100)

    print((test.array))


main()
