from dequeue import *

def isPalindrome(str):
    deq = Deque()
    for i in range(len(str)):
        deq.addFront(str[i])

    while deq.size() > 1:
        if deq.removeFront() == deq.removeTail():
            continue
        else:
            return False

    return True

print(isPalindrome("101"))

# TEST

def addFrontTest():
    print("addFront test")
    deq = Deque()
    deq.addFront(1)

    if deq.size() == 1 and deq.removeFront() == 1:
        print("OK")
    else:
        print("ERROR")

addFrontTest()

def addTailTest():
    print("addTail test")
    deq = Deque()
    deq.addFront(1)
    deq.addFront(2)

    if deq.size() == 2 and deq.removeTail() == 1:
        print("OK")
    else:
        print("ERROR")

addTailTest()

def removeFrontTest():
    print("removeFront test")
    deq = Deque()
    deq.addFront(1)
    a = deq.removeFront()

    if deq.size() == 0 and a == 1:
        print("OK")
    else:
        print("ERROR")

removeFrontTest()

def removeTailTest():
    print("removeTail test")
    deq = Deque()
    deq.addFront(1)
    deq.addFront(2)
    a = deq.removeTail()

    if deq.size() == 1 and a == 1:
        print("OK")
    else:
        print("ERROR")

removeTailTest()