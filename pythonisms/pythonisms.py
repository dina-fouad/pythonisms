from functools import wraps

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class LinkedList:

    def __init__(self, collection=None):
        self.head = None

        if collection:
            for item in reversed(collection):
                self.insert(item) 

    def __iter__(self):
     def generator():
      current = self.head
      while current:
        yield current.value
        current = current.next
     return generator()

    def __str__(self):
        out = ""
        for value in self:
            out += f"[ {value} ] -> "
        return out + "None"

    def __len__(self):
        return len(list(iter(self)))

   

    def __getitem__(self, index):
        if index < 0:
            index = len(self) + index

        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError


    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next
            current.next = node

    def proclaim(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return "On this day I do say, " + orig_val

      return wrapper