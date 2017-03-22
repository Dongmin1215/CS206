class Node(object):
    def __init__(sel):
        self.next = None
        self.previous = None

    def set_next():
        self.next = None

    def get_next():
        return sefl.next

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
            string = string +"" + str(point.other)
            point = point.next
        return string

list1 = List()
list1.append(3)
print(list1)
