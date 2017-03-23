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
            string = string +"" + str(point)
            point = point.next
        return string

class Queue(List):
    def enque(self,value):
        self.append(value)

    def deque(self):
        self.temp = self.first
        self.first = self.first.next
        return self.temp

class Stack(List):
    def push(self,value):
        self.append(value)

    def pop(self):
        self.temp = self.last
        print(self.temp)
        self.last = self.last.previous
        return self.temp



queue_1 = Queue()
queue_2 = Queue()
queue_3 = Queue()

valid = True

while valid:
    raw_input = input()
    for i in range(len(raw_input)):
        if "3" == raw_input[i]:
            queue_3.append(raw_input)
        if "2" == raw_input[i]:
            queue_2.append(raw_input)
        if "1" == raw_input[i]:
            queue_1.append(raw_input)
    if raw_input == "done":
        valid = False


print(queue_1,queue_2, queue_3)

 
