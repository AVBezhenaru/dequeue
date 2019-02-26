class Deque:
    def __init__(self):
        self.dequeue = []

    def addFront(self, item):
        self.dequeue.insert(0, item)

    def addTail(self, item):
        self.dequeue.append(item)

    def removeFront(self):
        if self.dequeue == []:
            return None
        return self.dequeue.pop(0)

    def removeTail(self):
        if self.dequeue == []:
            return None
        return self.dequeue.pop()

    def size(self):
        return len(self.dequeue)