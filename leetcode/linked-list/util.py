class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(nums):
    dummy = ListNode()
    curr = dummy

    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next


def build_cycle(nums, pos):
    nodes = [ListNode(x) for x in nums]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


def print_list_node(head):
    while head:
        print(head.val)
        head = head.next
