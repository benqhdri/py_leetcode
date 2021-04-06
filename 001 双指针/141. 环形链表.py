# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        i = head
        j = head
        while i and j and j.next:
            i = i.next
            j = j.next.next

            if i == j:
                return True
        return False


if __name__ == '__main__':
    head = ListNode(1)
    n1 = ListNode(2)
    head.next = n1
    print(Solution().hasCycle(head))
