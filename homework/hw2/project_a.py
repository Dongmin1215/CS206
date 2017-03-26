#make a node
class Node(object): 
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None
        self.top = None

    def __str__(self):
        return str(self.value)

#make a class of List
class List(object):
    def __init__(self):
        self.first = None
        self.last = None

    #make a method
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
#define a Queue 
class Queue(List):
    def enque(self,value):
        self.append(value)

    def deque(self):
        self.temp = self.first
        self.first = self.first.next
        return self.temp

#define a Stack
class Stack(List):
    def push(self,value):
        self.append(value)

    def pop(self):
        self.temp = self.last
        self.last = self.last.previous
        return self.temp.value

#define a function which calculate the infix

#idea of the function
#when the current(variable) meets the number -> then the read_num functions begin and push the number in the num_stack
#when the current meets the '(' -> calcuate the phrase (in the bucket)


def evaluate(infix):
    #create a stack
    num_stack = Stack()
    num_stack.push(12313)

    #since we can put only integer in the stack we choose the "LEFT" to be an integer
    LEFT = 10000000
    infix = '(%s)' %infix

    #define a function that finds whether ii is operator or not
    def is_op(op):
        return op == '+' or op == '-' or op == '*' or op == '/' or op == '(' or op == ')'

    #define a function that reads the current of the infix expression
    def read_num(cur):
        if infix[cur] == '(':
            return read_phrase(cur)
        #save the number in the ret
        ret = 0
       #since the number can be larger than 10
        while not is_op(infix[cur]):
            ret *= 10
            ret += int(infix[cur])
            cur += 1
        num_stack.push(ret)

        return cur

    #define a function if the current is not a number and calculate the infix expression
    def read_phrase(cur):
        #to push the '(' (=LEFT) for the calculating the first expression 
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
               #we will sum everything in the num_stack so '+' doesn't need any calculation
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

    #give the notice of the zero divition
    try:
        read_num(0)
    except ZeroDivisionError:
        print("Zero Division!!!!")
        return None
    return num_stack.pop()



if __name__ == '__main__':
    expr1 = '1+(2+3)'
    expr2 = '((3+5)*((16/3)-2))'

    print("%s = %d" %(expr1, evaluate(expr1)))
    print("%s = %d" %(expr2, evaluate(expr2)))



