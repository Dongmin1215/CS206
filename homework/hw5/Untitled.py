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

    def pop(self):
        return self.items.pop()

class Entry(object):
    def __str__(self):
        return '\n'.join(self.string())

    def __repr__(self):
        return 'Entry()'

    def string(self):
        return NotImplemented

class NoneEntry(Entry):
    def __repr__(self):
        return 'NoneEntry()'



class TreeEntry(Entry):
    def __init__(self, value):
        self.__left = NoneEntry()
        self.__right = NoneEntry()
        self.__value = value

    def __repr__(self):
        return 'TreeEntry(%s)' %self.value()

    def string(self):
        result = [str(self.value())]
        try:
            left_string = ['|    %s' %string for string in self.left().string()]
            left_string[0] = '|___ ' + left_string[0][5:]
            result += left_string
        except AssertionError:
            pass
        try:
            right_string = ['     %s' %string for string in self.right().string()]
            right_string[0] = '|___ ' + right_string[0][5:]
            result += ['|'] + right_string
        except AssertionError:
            pass
        return result

    # Getter and setter of the left node
    def left(self, entry=None):
        if isinstance(entry, Entry):
            self.__left = entry
            return self

        #assert not isinstance(self.__left, NoneEntry)

        return self.__left

    # Getter and setter of the right node
    def right(self, entry=None):
        if isinstance(entry, Entry):
            self.__right = entry
            return self

       # assert not isinstance(self.__right, NoneEntry)

        return self.__right

    # getter and setter of the value
    def value(self, v=None):
        if v is None:
            return self.__value

        self.__value = v
        return self

# Make a tree.
class Tree(object):
    def __init__(self, root=NoneEntry()):
        self.__root = root

    def __str__(self):
        return str(self.root())

    # getter and setter of the root leaf.
    def root(self, entry=None):
        if isinstance(entry, Entry):
            self.__root = entry
            return self

#        assert not isinstance(self.__root, NoneEntry)

        return self.__root



def is_op(op):
    return op == '+' or op == '-' or op == '*' or op == '/' or op == '(' or op == ')'


def infix_to_postfix(infix):
    num_stack = Stack()

    op_stack = Stack()
    infixlist = []
    infixlist_int = []
    global postfixlist
    postfixlist = []
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1


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

    for oper in infixlist:
        if not is_op(oper):
            postfixlist.append(str(oper))
        elif oper == '(':
            op_stack.push(oper)
        elif oper == ')':
            topoper = op_stack.pop()
            while topoper != '(':
                postfixlist.append(str(topoper))
                topoper = op_stack.pop()
        else:
            while (not op_stack.isEmpty()) and (prec[op_stack.peek()] >= prec[oper]):
                postfixlist.append(str(op_stack.pop()))
            op_stack.push(oper)

    while not op_stack.isEmpty():
        postfixlist.append(str(op_stack.pop()))



if __name__ == '__main__':
    expr1 = '((54+37)/(72-(5*13)))'

    print("%s = %s" %(expr1, infix_to_postfix(expr1)))
    print(postfixlist)
    stack = Stack()
    for token in postfixlist:
        if not is_op(token):
            stack.push(token)
        else:
            tree = Tree(TreeEntry(token).left(stack.pop()).right(stack.pop()))
            stack.push(tree)
            print(tree)


