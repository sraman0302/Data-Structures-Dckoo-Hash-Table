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
        return (array.count(None)+array.count("K.A."))

    def member(self, val, array):
        size = len(array)
        H = self.value(val, size)
        i = 0
        while(array[(H+i) % size] != None and i < size):
            if(array[(H+i) % size] == val):
                return ((H+i) % size)
            i += 1
        return None

    def load_factor(self, array, size):
        currcapacity = self.capacity(array)
        lf = ((size-currcapacity)/size)
        return lf

    def bin(self, index):
        return (self.array[index])
# Mutators

    def insert(self, val):
        pos = self.member(val, self.array)
        if(pos == None):
            self.array = self.Cuckoo(self.array, val)
        else:
            print("Value {} already present at position {} ".format(val, pos+1))

    def changeSize(self, array, size):

        newArray = [None]*(size)

        for element in array:
            if ((element != None) and (element != "K.A")):
                H = self.value(element, size)
                i = 0
                while(newArray[(H+i) % size] != None):
                    i += 1
                newArray[H] = element
            else:
                continue
        return(newArray)

    def remove(self, val):
        index = self.member(val, self.array)
        array = self.array
        size = len(array)
        if(index == None):
            print("Value not Present")
            return False

        else:
            array[index] = "K.A."
            lf = round(self.load_factor(array, size), 2)
            if (lf < 0.25):
                array = self.changeSize(array, size/2)
            self.array = array
            return True

    def clear(self):
        self.array = []*self.count
        return(self.array)

    def value(self, val, size):
        newVal = val*53267
        if(newVal <= 0):
            newVal = (newVal+(2**31))
        bit = bin(newVal)
        bit = bit[:-5]
        newVal = int(bit, 2)

        H = newVal % size

        return (H)

    def Cuckoo(self, array, val):
        size = self.size(array)
        H = self.value(val, size)
        lf = round(self.load_factor(array, size), 2)
        if (lf > 0.75):
            array = self.changeSize(array, size*2)
        i = 0
        while(((array[(H+i) % size] != None) and (array[(H+i) % size] != "K.A."))and i < size):
            i += 1
        array[(H+i) % size] = val

        return(array)
# Destructor

#    def __del__(self):
 #       print("Deleted")


def main():
    print()
    test = Dynamic_linear_hash_table(16)

    a = []
    for i in range(0, 15):
        a.append(random.randint(1, 100))
    for element in a:
        test.insert(element)

    """
    test.insert(1)
    test.insert(53)
    test.insert(93)
    test.insert(100)
    test.remove(100)
    test.insert(100)
    """
    print(len(test.array))


main()
