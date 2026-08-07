# Design Dynamic Array (Resizable Array)

# Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

# Your DynamicArray class should support the following operations:

# DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
# int get(int i) will return the element at index i. Assume that index i is valid.
# void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
# void pushback(int n) will push the element n to the end of the array.
# int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
# void resize() will double the capacity of the array.
# int getSize() will return the number of elements in the array.
# int getCapacity() will return the capacity of the array.

# If we call pushback(int n) but the array is full, we should resize() the array first.

# Note:

# The index i provided to get(int i) and set(int i) is guaranteed to be greater than or equal to 0 and less than the number of elements in the array.


class DynamicArray:

    def __init__(self, capacity: int = 4):
        self.length = 0
        self.capacity = capacity
        self.arr = [None] * capacity

    def __getitem__(self, i: int) -> int:
        self._check_index(i)
        return self.arr[i]

    def __setitem__(self, i: int, n: int) -> None:
        self._check_index(i)
        self.arr[i] = n

    def __len__(self) -> int:
        return self.length

    def __repr__(self):
        return str(self.arr[: self.length])

    def __contains__(self, value):
        for i in range(self.length):
            if self.arr[i] == value:
                return True
        return False

    def __bool__(self):
        return self.length > 0

    def getCapacity(self) -> int:
        return self.capacity

    def pushback(self, n: int) -> None:
        self.resize()
        self.arr[self.length] = n
        self.length = self.length + 1

    def back(self) -> int:
        self._check_not_empty()
        return self.arr[self.length - 1]

    def popback(self) -> int:
        self._check_not_empty()

        last_element = self.arr[self.length - 1]
        self.arr[self.length - 1] = None
        self.length = self.length - 1

        self.resize()
        return last_element

    def _resize(self) -> None:
        if self.length <= self.capacity / 4:
            new_capacity = max(4, self.capacity // 2)
        elif self.length == self.capacity:
            new_capacity = self.capacity * 2
        else:
            return
        new_arr = [None] * new_capacity
        new_arr[: self.length] = self.arr[: self.length]
        self.arr = new_arr
        self.capacity = new_capacity

    def _check_not_empty(self):
        if self.length == 0:
            raise IndexError("operation from empty DynamicArray")

    def _check_index(self, i: int = 0):
        if i < 0 or self.length <= i:
            raise IndexError("index out of boundry")
