class Elem:
    def __init__(self, data):
        self.data = data
        self.link_next = None

class LinkedList:
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

