class Stack:
    def __init__(self,itemlist=[]):
        self.items = itemlist

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[-1:][0]

    def push(self, value):
        self.items.append(value)
        return 0

    def pop(self):
        return self.items.pop()

def infix_to_postfix(infix):

    num_stack = Stack()
    num_stack.push(100000)
    op_stack = Stack()
    infixlist = []
    infixlist_int = []
    postfixlist = []

    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    def is_op(op):
        return op == '+' or op == '-' or op == '*' or op == '/' or op == '(' or op == ')'

    def read_num(cur):
        if infix[cur] == '-':
            cur += 1
            cur = read_num(cur)
            num_stack.push(- num_stack,pop())
        
        ret = 0
        while not is_op(infix[cur]):
            ret *= 10
            ret += int(infix[cur])
            cur += 1
        num_stack.push(ret)
        infixlist.append(str(ret))
        infixlist_int.append(ret)
        return cur

    
    curr = 0
    while curr < len(infix):
        if is_op(infix[curr]):
            infixlist.append(infix[curr])
            infixlist_int.append(infix[curr])
        else:
            read_num(curr)
            numb = num_stack.pop()
            while numb > 10:
                curr += 1
                numb = numb // 10
        curr += 1

    

    def convert(infix):
        for oper in infixlist:
            if not is_op(oper):
                postfixlist.append(oper)
            elif oper == '(':
                op_stack.push(oper)
            elif oper == ')':
                topoper = op_stack.pop()
                while topoper != '(':
                    postfixlist.append(topoper)
                    topoper = op_stack.pop()
            else:
                while (not op_stack.isEmpty()) and \
                        (prec[op_stack.peek()] >= prec[oper]):
                            postfixlist.append(op_stack.pop())
                            op_stack.push(oper)

        while not op_stack.isEmpty():
            postfixlist.append(op_stack.pop())
        return " ".join(postfixlist)
    
    print(infixlist)
    print(infixlist_int)
if __name__ == '__main__':
    expr1 = '(61+(2*3))'

    print("%s = %s" %(expr1, infix_to_postfix(expr1)))


