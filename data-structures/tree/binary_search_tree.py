from tree_node import TreeNode


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, val: int = 0) -> None:
        new_node = TreeNode(val)

        if self.root is None:
            self.root = new_node
            return

        curr = self.root
        while curr:
            if curr.val < val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = new_node
                    return
            elif curr.val > val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = new_node
                    return
            else:
                return

    def search(self, val: int) -> TreeNode | None:
        # Recursive version
        # return self._search(self.root, val)

        if self.root is None:
            return None

        curr = self.root
        while curr:
            if curr.val < val:
                curr = curr.right
            elif curr.val > val:
                curr = curr.left
            else:
                return curr

        return None

    def _search(self, node: TreeNode | None, val: int) -> TreeNode | None:
        if node is None:
            return None
        elif node.val < val:
            return self._search(node.right, val)
        elif node.val > val:
            return self._search(node.left, val)
        else:
            return node

    def min(self) -> TreeNode | None:
        # Recursive version
        # return self._min(self.root)

        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr

    def _min(self, node: TreeNode | None) -> TreeNode | None:
        if node is None or node.left is None:
            return node
        return self._min(node.left)

    def max(self) -> TreeNode | None:
        # Recursive version
        # return self._max(self.root)

        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr

    def _max(self, node: TreeNode | None) -> TreeNode | None:
        if node is None or node.right is None:
            return node
        return self._max(node.right)

    def delete(self, val: int) -> bool:
        if self.search(val) is None:
            return False

        self.root = self._delete(self.root, val)
        return True

    def _delete(self, node: TreeNode | None, val: int) -> TreeNode | None:
        if node is None:
            return None
        elif val < node.val:
            node.left = self._delete(node.left, val)
            return node
        elif val > node.val:
            node.right = self._delete(node.right, val)
            return node
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                successor = self._min(node.right)
                node.val = successor.val
                node.right = self._delete(node.right, successor.val)
                return node

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node: TreeNode | None) -> int:
        if node is None:
            return -1

        return max(self._height(node.left), self._height(node.right)) + 1

    def inorder(self) -> list:
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: TreeNode, result: list) -> None:
        if node is None:
            return

        self._inorder(node.left, result)
        result.append(node.val)
        self._inorder(node.right, result)


nums = [8, 3, 10, 1, 6, 14, 4, 7, 13]

bst = BinarySearchTree()
for n in nums:
    bst.insert(n)

# assert bst.inorder() == [1, 3, 4, 6, 7, 8, 10, 13, 14]
# assert bst.root.val == 8
# assert bst.root.left.val == 3
# assert bst.root.right.val == 10

# print("insert() passed!")

# assert bst.search(8).val == 8
# assert bst.search(1).val == 1

# assert bst.search(13).val == 13
# assert bst.search(100) is None
# assert bst.search(-5) is None

# print("search() passed!")

assert bst.min().val == 1

bst2 = BinarySearchTree()
assert bst2.min() is None

bst3 = BinarySearchTree()
bst3.insert(5)
assert bst3.min().val == 5

print("min() passed!")
