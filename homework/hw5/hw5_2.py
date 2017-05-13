import json

class Stack:
    def __init__(self):
        self.items = []

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

        assert not isinstance(self.__left, NoneEntry)

        return self.__left

    # Getter and setter of the right node
    def right(self, entry=None):
        if isinstance(entry, Entry):
            self.__right = entry
            return self

        assert not isinstance(self.__right, NoneEntry)

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

        assert not isinstance(self.__root, NoneEntry)

        return self.__root

def tree_dict(tree):
    a = {}
    a['key'] = tree.value()
    try:
        tree.left()
        a['left'] = tree_dict(tree.left())
    except AssertionError:
        pass

    try:
        tree.right()
        a['right'] = tree_dict(tree.right())
    except AssertionError:
        pass

    return a

def dict_tree(dic):
    tree = Tree()
    tree = TreeEntry(dic['key'])

    if 'left' in dic:
        tree.left(dict_tree(dic['left']))

    if 'right' in dic:
        tree.right(dict_tree(dic['right']))
    return tree


dic = {'key':'cat', 'left': {'key':'apple', 'right' : {'key': 'but'}}, 'right' : {'key' : 'but'}}


if __name__ == '__main__':
    tree = TreeEntry('cat').left(TreeEntry('apple').right(TreeEntry('but'))).right(TreeEntry('pull').left(TreeEntry('line').left(TreeEntry('food')).right(TreeEntry('me'))).right(TreeEntry('say')))
    print(tree)
    print(tree_dict(tree))
    print(dict_tree(dic))
