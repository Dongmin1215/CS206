class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

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
    def __str__(self):
        string = ""
        point = self.first
        while point != None:
            string = string +" " + str(point)
            point = point.next
        return string

def Stack(List):
    def push(self,value):
        self.append(value)

    def pop(self):
        self.temp = self.last
        print(self.temp)
        self.last = self.last.previous

def Queue(List):
    def enque(self, value):
        self.append(value)

    def deque(self):
        self.temp = self.first
        self.first = self.first.next
        return self.temp


