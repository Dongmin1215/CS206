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
        self.last = self.last.previous
        return self.temp.value


def evaluate(infix):
    num_stack = Stack()
    num_stack.push(12313)

    LEFT = 103941049012
    infix = '(%s)' %infix

    def is_op(op):
        return op == '+' or op == '-' or op == '*' or op == '/' or op == '(' or op == ')'


    def read_num(cur):
        if infix[cur] == '(':
            return read_phrase(cur)
        ret = 0
        while not is_op(infix[cur]):
            ret *= 10
            ret += int(infix[cur])
            cur += 1
        num_stack.push(ret)

        return cur

    def read_phrase(cur):
        num_stack.push(LEFT)

        while True:
            if infix[cur] == ')':
                a = num_stack.pop()
                summ = 0
                while a != LEFT:
                    summ += a
                    a = num_stack.pop()
                num_stack.push(summ)
                cur += 1
                return cur
            else:
                cur += 1
                cur = read_num(cur)
                if infix[cur] == '+':
                    pass
                elif infix[cur] == '-':
                    cur += 1
                    cur = read_num(cur)
                    num_stack.push(-num_stack.pop())
                elif infix[cur] == '*':
                    cur += 1
                    cur = read_num(cur)
                    num_stack.push(num_stack.pop() * num_stack.pop())
                elif infix[cur] == '/':
                    cur += 1
                    cur = read_num(cur)
                    a = num_stack.pop()
                    b = num_stack.pop()
                    num_stack.push(int(b / a))

    try:
        read_num(0)
    except ZeroDivisionError:
        print("Zero Division!!!!")
        return None
    return num_stack.pop()


            

if __name__ == '__main__':
    expr1 = '1+(2+3)'
    expr2 = '((3+5)*((16/3)-2))'

    print("%s = %d (%d)" %(expr1, evaluate(expr1), int(eval(expr1))))
    print("%s = %d (%d)" %(expr2, evaluate(expr2), int(eval(expr2))))



