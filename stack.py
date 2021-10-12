"""
Stack

>>> stack = Stack()
>>> stack.size
0
>>> stack.pop()
Traceback (most recent call last):
    ...
IndexError: pop from empty stack
>>> stack.push('a')
>>> stack.push('b')
>>> stack.size
2
>>> stack.pop()
'b'
>>> stack.size
1
>>> stack.push('c')
>>> stack.size
2
>>> stack.peek()
'c'
>>> stack.size
2
>>> stack.pop()
'c'
>>> stack.size
1
>>> stack.pop()
'a'
>>> stack.size
0
>>> stack.pop()
Traceback (most recent call last):
    ...
IndexError: pop from empty stack
>>> stack.peek()
Traceback (most recent call last):
    ...
IndexError: peek from empty stack

>>> stack.size = 3
Traceback (most recent call last):
    ...
AttributeError: can't set attribute
"""


class Elem:
    def __init__(self, data):
        self.data = data
        self.link_next = None


class Stack:
    def __init__(self):
        self._elems = {}
        self._link_first = None
        self._size = 0

    def push(self, data):
        elem_new = Elem(data)
        link_new = id(elem_new)
        self._elems[link_new] = elem_new
        elem_new.link_next = self._link_first
        self._link_first = link_new
        self._size += 1

    def pop(self):
        link_first = self._link_first
        if not link_first:
            raise IndexError('pop from empty stack')
        elem_first = self._elems[link_first]
        data = elem_first.data
        self._link_first = elem_first.link_next
        del self._elems[link_first]
        self._size -= 1
        return data

    @property
    def size(self):
        return self._size

    def peek(self):
        if not self._link_first:
            raise IndexError('peek from empty stack')
        return self._elems[self._link_first].data
