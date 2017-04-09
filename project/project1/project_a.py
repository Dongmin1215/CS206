class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        self.top = None

    def __str__(self):
        return str(self.value)

class List(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.__len = 0 

    def append(self, value):
        node = Node(value)
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            node.previous = self.last
            self.last = node
        self.__len += 1

    def set(self, index, value):
        if not isinstance(index, int):
            raise IndexError

        cur = self.first
        for i in range(index):
            if cur is None:
                raise IndexError
            cur = cur.next
        if cur is None:
            raise IndexError
        cur.value = value

    def eq(self, other):
        if not isinstance(other, List):
            return False
        if not len(self) == len(other):
            return False
        for i in range(len(self)):
            if not self[i] == other[i]:
                return False

        return True

    __eq__ = eq

    def __repr__(self):
        string = ''
        point = self.first

        if not point is None:


