class Elem:
    def __init__(self, data):
        self.data = data
        self.link_next = None

class LinkedList:
    """
    >>> ll = LinkedList()
    >>> ll.get_array()  # empty list
    []
    >>> ll.insert(0, 'd')  # first element
    >>> ll.get_array()
    ['d']
    >>> ll.insert(0, 'b')  # new first element before 'd'
    >>> ll.get_array()
    ['b', 'd']
    >>> ll.insert(1, 'c')
    >>> ll.get_array()
    ['b', 'c', 'd']
    >>> ll.insert(-10, 'a')  # new first element
    >>> ll.get_array()
    ['a', 'b', 'c', 'd']
    >>> ll.insert(10, 'e')  # last element
    >>> ll.get_array()
    ['a', 'b', 'c', 'd', 'e']

    >>> ll = LinkedList()  # new list
    >>> ll.get_array()
    []
    >>> ll.insert(-10, 'a')  # -10, but 'a' is first element in new list
    >>> ll.get_array()
    ['a']

    >>> ll = LinkedList()  # new list
    >>> ll.get_array()
    []
    >>> ll.insert(10, 'b')  # 10, but 'b' is first element in new list
    >>> ll.get_array()
    ['b']
    """
    def __init__(self):
        self._linked_list = {}
        self._link_first = None

    def insert(self, index, data):
        elem_new = Elem(data)
        link_new = id(elem_new)
        if index < 1 or not self._link_first:
            if self._link_first:
                elem_new.link_next = self._link_first
            self._linked_list[link_new] = elem_new
            self._link_first = link_new
            return
        link = self._link_first
        elem_before = self._linked_list[link]
        for _ in range(index-1):
            link = elem_before.link_next
            if not link:
                break
            elem_before = self._linked_list[link]
        link_next = elem_before.link_next
        elem_new.link_next = link_next
        self._linked_list[link_new] = elem_new
        elem_before.link_next = link_new

    def get_array(self):
        result = []
        link = self._link_first
        while link:
            elem = self._linked_list[link]
            result.append(elem.data)
            link = elem.link_next
        return result
