class Node(object):
    def __init__(self,value):
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

    def append(self, value):
        node = Node(value)
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            node.previous = self.last
            self.last = node

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


    def __repr__(self):
        string = ""
        point = self.first

        if not point is None:
            string = str(point)
            point = point.next
            while not point is None:
                string = string +", " + str(point)
                point = point.next

        return "[%s]" %string

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise IndexError

        cur = self.first
        for i in range(index):
            if cur is None:
                raise IndexError
            cur = cur.next
        if cur is None:
            raise IndexError

        return cur.value

class Matrix(List):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        super(Matrix, self).__init__()
        
        for i in range(x):
            l = List()
            for j in range(y):
                l.append(0)
            self.append(l)

    def __repr__(self):
        string = ""
        for i in range(self.x()):
            string += "%s\n" %self[i]
        return string

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def set(self, x, y, value):
        self[x].set(y, value)

    def add(self, other):
        if not isinstance(other, Matrix):
            raise ValueError
        if not (self.x() == other.x() and self.y() == other.y()):
            raise ValueError

        ret = Matrix(self.x(), self.y())

        for i in range(self.x()):
            for j in range(self.y()):
                ret.set(i, j, self[i][j] + other[i][j])

        return ret

    __add__ = add


if __name__ == '__main__':
    import random

    a = Matrix(5, 5)
    b = Matrix(5, 5)

    for i in range(5):
        for j in range(5):
            a.set(i, j, random.randint(0, 5))
            b.set(i, j, random.randint(0, 5))

    print "a = \n%s" %a
    print "b = \n%s" %b
    print "a + b = \n%s" %(a+b)
