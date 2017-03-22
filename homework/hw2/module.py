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

list1 = List()
for i in range(10): 
    list1.append(i)
print(list1)
