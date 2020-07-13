import sys
from math import pow


class Dynamic_linear_hash_table:
    def __init__(self, count):
        self.name = None
        self.count = int(pow(2, count))
        self.initCapacity = int(pow(2, count))
        self.currCapacity = int(pow(2, count))
        self.array = [None]*int(pow(2, count))

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
            if (lf <= 0.25):
                array = self.changeSize(array, size/2)
            self.array = array
            return True

    def clear(self):
        self.array = []*self.count
        return(self.array)

    def value(self, val, size):
        newVal = val*53267
        if(newVal <= 0):
            newVal = (newVal+(int(pow(2, 31))))
        bit = bin(newVal)
        bit = bit[:-5]
        newVal = int(bit, 2)

        H = newVal % size

        return (H)

    def Cuckoo(self, array, val):
        size = self.size(array)
        H = self.value(val, size)
        lf = round(self.load_factor(array, size), 2)
        if (lf >= 0.75):
            array = self.changeSize(array, size*2)
        i = 0
        while(((array[(H+i) % size] != None) and (array[(H+i) % size] != "K.A."))and i < size):
            i += 1
        array[(H+i) % size] = val

        return(array)
# Destructor

    def __del__(self):
        print("Deleted")

# Functions


def create():
    m = input("Enter size or use ENTER for default value (3) ")
    try:
        m = int(m)
        while(m < 2):
            m = int(input("Enter size not less than 2"))

    except:
        m = 3

    obj = Dynamic_linear_hash_table(m)
    return (obj)


def printTable(object):
    i = 1
    for obj in object:
        print(i, ". ", obj.array)
        i += 1


def insert(object):
    printTable(object)
    i = int(input("Which ith Hash Table to insert value "))
    val = int(input("Enter value: "))
    object[i-1].insert(val)
    return object


def size(object):
    printTable(object)
    i = int(input("Which ith Hash Table to view size "))
    print("Size:", object[i-1].size(object[i-1].array))


def Capacity(object):
    printTable(object)
    i = int(input("Which ith Hash Table to view capacity "))
    print("Capacity: ", object[i-1].capacity(object[i-1].array))


def Remove(object):
    printTable(object)
    i = int(input("Which ith Hash Table to remove value "))
    val = int(input("Enter value: "))
    object[i-1].remove(val)
    return object


def Empty(object):
    printTable(object)
    i = int(input("Which ith Hash Table to view if empty: "))
    val = object[i-1].capacity()
    if(val == True):
        print("Hash Table Empty")
    else:
        print("Hash Table Not Empty")


def Bin(object):
    printTable(object)
    i = int(input("Which ith Hash Table to Bin value "))
    index = int(input("Enter Bin Number: "))
    print("Value:", object[i-1].bin(index))


def LF(object):
    printTable(object)
    i = int(input("Which ith Hash Table to view Load Factor "))
    print("Load Factor:", object[i-1].load_factor(object[i-1].array()))


def member(object):
    printTable(object)
    i = int(input("Which ith Hash Table to view member Bin "))
    val = int(input("Enter value to search: "))
    print("Member is at Bin:", object[i-1].member(val, object[i-1].array()))


def clear(object):
    printTable(object)
    i = int(input("Which ith Hash Table to clear "))
    object[i-1] = object[i-1].clear(object[i-1].array())
    return object


def delete(object):
    printTable(object)
    i = int(input("Which ith Hash Table to delete "))
    del object[i-1]
    object.pop(i-1)
    return object


def main():

    object = []

    mainChoice = True

    while(mainChoice == True):
        print("Main Menu")
        print("(1) Create New Hash Table ")
        print("(2) Print Hash Tables Created")
        print("(3) Insert Value")
        print("(4) Size of the Hash Table")
        print("(5) Capacity of Hash Table")
        print("(6) Remove Value")
        print("(7) Check Hash Table is Empty")
        print("(8) Element in Bin X")
        print("(9) Load Factor")
        print("(10) Member Search")
        print("(11) Clear Hash Table")
        print("(12) Delete Hash Table")
        print("(13) Exit")

        command = int(input("Your Command: "))

        if(command > 13 or command < 1):
            print("Invalid Command")

        if(command == 1):
            obj = create()
            object.append(obj)

        elif(command == 2):
            if(len(object) > 0):
                printTable(object)
            else:
                print("There's no object created")
                ch = input("Create one now? (Y/N)")
                ch = ch.upper()
                if(ch == "Y"):
                    obj = create()
                    object.append(obj)
        elif(command == 3):
            if(len(object) > 0):
                object = insert(object)
            else:
                print("There's no object created")
                ch = input("Create one now? (Y/N)")
                ch = ch.upper()
                if(ch == "Y"):
                    obj = create()
                    object.append(obj)
        elif(command == 4):
            if(len(object) > 0):
                object = size(object)
            else:
                print("There's no object created")
                ch = input("Create one now? (Y/N)")
                ch = ch.upper()
                if(ch == "Y"):
                    obj = create()
                    object.append(obj)
        elif (command == 5):
            if(len(object) > 0):
                object = Capacity(object)
            else:
                print("There's no object created")
                ch = input("Create one now? (Y/N)")
                ch = ch.upper()
                if(ch == "Y"):
                    obj = create()
                    object.append(obj)
        elif (command == 6):
            if(len(object) > 0):
                object = Remove(object)
            else:
                print("There's no object created")
                ch = input("Create one now? (Y/N)")
                ch = ch.upper()
                if(ch == "Y"):
                    obj = create()
                    object.append(obj)
        elif(command == 7):
            if(len(object) > 0):
                object = Empty(object)
            else:
                print("There's no object created")
                ch = input("Create one now? (Y/N)")
                ch = ch.upper()
                if(ch == "Y"):
                    obj = create()
                    object.append(obj)
        elif(command == 8):
            if(len(object) > 0):
                Bin(object)
            else:
                print("There's no object created")
                ch = input("Create one now? (Y/N)")
                ch = ch.upper()
                if(ch == "Y"):
                    obj = create()
                    object.append(obj)
        elif(command == 9):
            if(len(object) > 0):
                object = LF(object)
            else:
                print("There's no object created")
                ch = input("Create one now? (Y/N)")
                ch = ch.upper()
                if(ch == "Y"):
                    obj = create()
                    object.append(obj)
        elif(command == 10):
            if(len(object) > 0):
                object = member(object)
            else:
                print("There's no object created")
                ch = input("Create one now? (Y/N)")
                ch = ch.upper()
                if(ch == "Y"):
                    obj = create()
                    object.append(obj)

        elif(command == 11):
            if(len(object) > 0):
                object = clear(object)
            else:
                print("There's no object created")
                ch = input("Create one now? (Y/N)")
                ch = ch.upper()
                if(ch == "Y"):
                    obj = create()
                    object.append(obj)

        elif(command == 12):
            if(len(object) > 0):
                object = delete(object)
            else:
                print("There's no object created")
                ch = input("Create one now? (Y/N)")
                ch = ch.upper()
                if(ch == "Y"):
                    obj = create()
                    object.append(obj)

        elif(command == 13):
            print()
            print("Bye!")
            sys.exit()
        else:
            print("Invalid Command")


main()
