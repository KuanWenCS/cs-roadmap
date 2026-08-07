from tree_node import TreeNode


class BinaryTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __bool__(self) -> bool:
        return self.root is not None

    def is_empty(self) -> bool:
        return self.root is None

    def clear(self) -> None:
        self.root = None
        self.size = 0

    # DFS (Depth First Search)
    # Stack

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node: TreeNode | None) -> int:
        if node is None:
            return 0

        return max(self._height(node.left), self._height(node.right)) + 1

    def count_nodes(self) -> int:
        return self._count_nodes(self.root)

    def _count_nodes(self, node: TreeNode | None) -> int:
        if node is None:
            return 0

        return self._count_nodes(node.left) + self._count_nodes(node.right) + 1

    def count_leaves(self) -> int:
        return self._count_leaves(self.root)

    def _count_leaves(self, node: TreeNode | None) -> int:
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1

        return self._count_leaves(node.left) + self._count_leaves(node.right)

    def preorder(self) -> list:
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node: TreeNode, result: list) -> None:
        if node is None:
            return

        result.append(node.val)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

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

    def postorder(self) -> list:
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node: TreeNode, result: list) -> None:
        if node is None:
            return

        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.val)

    # BFS (Breadth First Search) aka Level Order Traversal
    # Queue

    def levelorder(self) -> list:
        if self.root is None:
            return []

        queue, result = [], []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            result.append(node.val)

        return result
