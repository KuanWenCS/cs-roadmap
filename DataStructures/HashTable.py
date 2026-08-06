class Node:

    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.bucket = [None] * capacity

    def hash(self, key: int) -> int:
        ascii_sum = 0
        for c in key:
            ascii_sum += ord(c)
        return ascii_sum % self.capacity

    def put(self, key: int, value: str) -> None:
        bucket_num = self.hash(key)
        if self.bucket[bucket_num] is None:
            self.bucket[bucket_num] = Node(key, value)
            self.size += 1
            return

        curr = self.bucket[bucket_num]
        while curr is not None:
            if curr.key == key:
                curr.value = value
                return
            prev = curr
            curr = curr.next
        prev.next = Node(key, value)
        self.size += 1
        return

    def get(self, key: int) -> str:
        bucket_num = self.hash(key)
        curr = self.bucket[bucket_num]
        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return curr

    def remove(self, key) -> bool:
        bucket_num = self.hash(key)
        curr = self.bucket[bucket_num]
        if curr is None:
            return False
        if curr.key == key:
            self.bucket[bucket_num] = curr.next
            self.size -= 1
            return True

        while curr is not None:
            if curr.key == key:
                prev.next = curr.next
                self.size -= 1
                return True
            prev = curr
            curr = curr.next
        return False

    def contains(self, key: int) -> bool:
        bucket_num = self.hash(key)
        curr = self.bucket[bucket_num]
        while curr is not None:
            if curr.key == key:
                return True
            curr = curr.next
        return False


ht = HashTable(5)

ht.put("John", 95)
assert ht.get("John") == 95

ht.put("John", 100)
assert ht.get("John") == 100

ht.put("Amy", 80)
assert ht.contains("Amy")

assert ht.remove("John") is True
assert ht.contains("John") is False

assert ht.remove("Kevin") is False
