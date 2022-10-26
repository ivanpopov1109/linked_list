class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            self.__next = next

    @next.deleter
    def next(self):
        del self.__next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:

    def __init__(self):
        self.top = None

    def get_last_obj(self, obj) -> StackObj:
        if obj == None:
            return
        if obj.next != None:
            return self.get_last_obj(obj.next)
        else:
            return obj

    def push_back(self, obj):
        if not self.top:
            self.top = obj
        else:
            last_obj = self.get_last_obj(self.top)
            last_obj.next = obj

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self

    def __imul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self

    def pop_back(self):
        last = self.get_last_obj(self.top)
        k = self.top
        if k == None:
            return
        if k == last:
            self.top = None
            return k
        while k.next != last:
            k = k.next
        k.next = None
        return k

    def get_data(self):
        l = []
        h = self.top
        while h:
            l.append(h.data)
            h = h.next
        return l
