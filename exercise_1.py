class Stack:

    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if len(self._items) == 0:
            raise PopEmptyStackException()
        self._items.pop()

class PopEmptyStackException(Exception):
    pass