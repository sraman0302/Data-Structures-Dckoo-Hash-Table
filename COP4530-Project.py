import random


class Dynamic_linear_hash_table:
    def __init__(self, count):
        self.name = None
        self.count = count
        self.initCapacity = count
        self.currCapacity = count
        self.array = [None]*count
        self.valuearray = []

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

    def member(self, val):
        if val in self.array:
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
        update = self.array
        self.array = self.Cuckoo(update, val)

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

    def value(self, val):
        newVal = val*53267
        if(newVal <= 0):
            newVal = (newVal+(2**31))
        bit = bin(newVal)
        bit = bit[:-5]
        newVal = int(bit, 2)
        return (newVal)

    def Cuckoo(self, array, val):
        newVal = self.value(val)
        size = self.capacity(array)
        H = newVal % size
        lf = self.load_factor(array)
        if (lf > 0.75):
            array = self.doubleSize(array)
        while(array[H] != None):
            H = H+1
        array[H] = val
        return(array)
# Destructor

#    def __del__(self):
 #       print("Deleted")


def main():
    print()
    test = Dynamic_linear_hash_table(16)
    a = []
    for i in range(0, 16):
        a.append(random.randint(1, 100))
    print(a)
    for element in a:
        test.insert(element)

    print((test.array))


main()
