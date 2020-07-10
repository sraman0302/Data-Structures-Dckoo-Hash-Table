class Dynamic_linear_hash_table:
    def __init__(self, count, currcapp, icapp):
        self.name = None
        self.count = count
        self.currCapacity = currcapp
        self.initCapacity = icapp

# Accessors

    def size(self):
        return self.count

    def empty(self):
        if (self.count == 0):
            return False
        else:
            return True

    def capacity(self, array):
        return (self.count-array.count(None))

    def member(self, val, array):
        if val in array:
            return True
        return False

    def load_factor(self, array):
        print()

    def bin(self, array):
        print()
# Mutators

    def insert(self):
        print()

    def remove(self):
        print()

    def clear(self):
        print()


def main():
    print()


main()
