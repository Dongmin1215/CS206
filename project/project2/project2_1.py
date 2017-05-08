# Import namedtuple
from collections import namedtuple


_sentinel = object()

# Make a Entry which works as a node
class Entry(object):
    def __str__(self):
        return '\n'.join(self.string())

    def __repr__(self):
        return 'Entry()'

    def string(self):
        return NotImplemented

# Entry which means null.
class NoneEntry(Entry):
    def __repr__(self):
        return 'NoneEntry()'

# Make a Tree.node
class TreeEntry(Entry):
    def __init__(self, value, left_e=NoneEntry(), right_e=NoneEntry()):
        self.__left = left_e
        self.__right = right_e
        self.__value = value

    def __repr__(self):
        return 'TreeEntry(%s)' %self.value

    def __or__(self, other):
        if isinstance(other.value, none):
            return none()

        if isinstance(other, left):
            if isinstance(other.value, Entry):
                left_e = other.value
            else:
                left_e = TreeEntry(other.value)
        else:
            left_e = getattr(self, 'left', NoneEntry())

        if isinstance(other, right):
            if isinstance(other.value, Entry):
                right_e = other.value
            else:
                right_e = TreeEntry(other.value)
        else:
            right_e = getattr(self, 'right', NoneEntry())

        return TreeEntry(self.value, left_e, right_e)

    # return the lis of string of each node
    def string(self):
        result = [str(self.value)]
        if hasattr(self, 'right'):
            right_string = ['|    %s' %string for string in self.right.string()]
            right_string[0] = '|___ ' + right_string[0][5:]
            result += right_string
        if hasattr(self, 'right'):
            left_string = ['     %s' %string for string in self.left.string()]
            left_string[0] = '|___ ' + left_string[0][5:]
            result += ['|'] + left_string
        return result

    # Getter and setter of the left node
    @property
    def left(self):
        if isinstance(self.__left, NoneEntry):
            raise AttributeError
        return self.__left

    # Getter and setter of the right node
    @property
    def right(self):
        if isinstance(self.__right, NoneEntry):
            raise AttributeError
        return self.__right

    # getter and setter of the value
    @property
    def value(self):
        return self.__value

    def is_leaf(self):
        return not (hasattr(self, 'left') or hasattr(self, 'right'))

    def flip(self):
        left_e = NoneEntry()
        right_e = NoneEntry()
        if hasattr(self, 'left'):
            left_e = self.left.flip()
        if hasattr(self, 'right'):
            right_e = self.right.flip()
        return self \
                | left(right_e) \
                | right(left_e)

    @classmethod
    def read_preorder(cls, preorder):
        assert len(preorder) > 0

        if '?' in preorder[0]:
            return cls(preorder.pop(0)) \
                    | left(cls.read_preorder(preorder)) \
                    | right(cls.read_preorder(preorder))
        return cls(preorder.pop(0))

# Make a tree.
class Tree(object):
    def __init__(self, root=_sentinel):
        assert not root is _sentinel

        if isinstance(root, TreeEntry):
            self.root = root
        else:
            self.root = TreeEntry(root)

    def __repr__(self):
        return 'Tree(%r)' %self.root

    def __str__(self):
        return str(self.root)

    # getter and setter of the root leaf.
    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, entry=None):
        if not isinstance(entry, TreeEntry):
            raise AttributeError
        self.__root = entry

    # Read the tree in preorder.
    def preorder(self):
        stack = [self.root]
        result = ''

        # stack means function call stack.
        while stack:
            cur = stack.pop()
            if hasattr(cur, 'right'):
                stack.append(cur.right)
            if hasattr(cur, 'left'):
                stack.append(cur.left)
            result += '%s\n' %cur.value

        return result

    # Read the tree in postorder.
    def postorder(self):
        FunctionCall = namedtuple('FunctionCall', ['entry', 'status'])
        stack = [FunctionCall(entry=self.root, status=0)]
        result = ''

        # stack means function call stack.
        while stack:
            cur = stack.pop()
            if cur.status == 0:
                stack.append(FunctionCall(entry=cur.entry, status=1))
                if hasattr(cur.entry, 'right'):
                    stack.append(FunctionCall(entry=cur.entry.right, status=0))
                if hasattr(cur.entry, 'left'):
                    stack.append(FunctionCall(entry=cur.entry.left, status=0))
            else:
                result += '%s\n' %cur.entry.value

        return result

    #read textfile that includes questions
    @classmethod
    def read_txt(cls, filename, preorder=True):
        with open(filename, 'r') as f:
            tree_list = [s.strip() for s in f.readlines()]
            return cls.read_preorder(tree_list) if preorder else cls.read_postorder(tree_list)

    #read textfile in preorder
    @classmethod
    def read_preorder(cls, tree_list):
        _tree_list = tree_list[:]
        ret = cls(TreeEntry.read_preorder(_tree_list))

        # if textfile is not in preorder raise error
        if len(_tree_list) > 0:
            raise SyntaxError('Invalid syntax')

        return ret

    # read textfile in postorder
    @classmethod
    def read_postorder(cls, tree_list):
        _tree_list = tree_list[::-1]
        ret = cls(TreeEntry.read_preorder(_tree_list).flip())

        # if textfile is not in postorder raise error
        if len(_tree_list) > 0:
            raise SyntaxError('Invalid syntax')

        return ret
# Make a class that makes an option
class Option(object):
    def __init__(self, value=None):
        self.__value = value

    # getter and setter of the value
    @property
    def value(self):
        return self.__value

class none(Option):
    pass

class prev(Option):
    pass

class some(Option):
    pass

class right(some):
    pass

class left(some):
    pass

# make a quiz game
def quiz(tree):
    def ask(prompt, Y=lambda: none(), N=lambda: none()):
        ans = input(prompt)
        if ans == 'Y':
            return Y()
        elif ans == 'N':
            return N()
        return ask(prompt, Y, N)

    # turn prev into none, and turn none into none_case
    def return_process(ret, none_case):
        if isinstance(ret, none):
            return none_case()
        elif isinstance(ret, prev):
            return none()
        return ret

    # make a traversal
    def traversal(cur):
        if cur.is_leaf():

            # define a function that ask the question when the user answers N in the last question
            def ask_name():
                entry = input('I give up. What are you? ')
                print(f'Please type a yes/no question that will distinguish a { entry } from a { cur.value }')
                question = input('Your question: ')
                return ask(f'As a { entry }, { question } Please answer [Y or N] ',
                           lambda: TreeEntry(question) \
                                   | left(entry) \
                                   | right(cur),
                           lambda: TreeEntry(question) \
                                   | left(cur) \
                                   | right(entry))
            return return_process(ask(f'My guess is { cur.value }. Am I right? [Y or N] ',
                                      lambda: cur,
                                      ask_name),
                                  lambda: traversal(cur))
        else:
            return return_process(ask(f'{ cur.value } [Y or N] ',
                                      lambda: cur \
                                              | left(traversal(cur.left)),
                                      lambda: cur \
                                              | right(traversal(cur.right))),
                                  lambda: traversal(cur))

    ret = return_process(traversal(tree.root), lambda: quiz(tree))

    return ask('Shall we play again? [Y or N] ',
               lambda: quiz(Tree(ret)),
               lambda: Tree(ret))

# the reason why the "save as" is beacuse when the user answers N in the last question, we get the answer of the user and the question that we can differetiate with the answer of the user and the expected answer and save it into new file 
code = """filename = input("Enter filename: ")
preorder = input("preorder or postorder: ")
if preorder in ('preorder', 'postorder'):
    is_preorder = True if preorder == 'preorder' else False
    t = quiz(Tree.read_txt(filename, is_preorder))
    new_filename = input("Save as: ")
    with open(new_filename, 'w') as f:
        f.write(t.preorder() if is_preorder else t.postorder())
    print(t)
"""


if __name__ == '__main__':
    print('######################################## CODE ########################################')
    print(code)
    print('######################################## RESULT ######################################')
    exec(code)
