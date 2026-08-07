from dynamic_array import DynamicArray


class Stack:

    def __init__(self):
        self.stack = DynamicArray()

    def push(self, value):
        self.stack.pushback(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.popback()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack.back()

    def is_empty(self) -> bool:
        return self.stack.getSize() == 0


# s = Stack()

# assert s.is_empty() == True
# assert s.size() == 0

# s.push(10)

# assert s.peek() == 10
# assert s.size() == 1
# assert s.is_empty() == False

# s.push(20)

# assert s.peek() == 20
# assert s.size() == 2

# assert s.pop() == 20
# assert s.peek() == 10
# assert s.size() == 1

# assert s.pop() == 10

# assert s.is_empty()
# assert s.size() == 0

# Test 6（空 Stack）
# try:
#     s.pop()
# except IndexError:
#     print("PASS")

# Test 7（大量資料）
# for i in range(1000):
#     s.push(i)

# assert s.size() == 1000

# for i in reversed(range(1000)):
#     assert s.pop() == i

# assert s.is_empty()
