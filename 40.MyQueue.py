class MyQueue:

    def __init__(self):

        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        self.stack1.append(element)

    """
    @return: An integer
    """

    def pop(self):
        self.top()
        return self.stack2.pop()

    """
    @return: An integer
    """

    def top(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


a = MyQueue()
a.push(1)
print(a.check())
print(a.pop())
# a.push(2)
# a.push(3)
# print(a.top())
# print(a.pop())