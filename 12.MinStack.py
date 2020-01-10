class MinStack:

    def __init__(self):
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        self.stack.append(number)

    """
    @return: An integer
    """

    def pop(self):

        return self.stack.pop()

    """
    @return: An integer
    """

    def min(self):
        return min(self.stack)
