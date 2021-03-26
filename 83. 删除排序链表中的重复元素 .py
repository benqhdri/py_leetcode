class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        双指针法，遇到第一个不重复的，直接指向它即可
        :param head:
        :return:
        """
        if not head or not head.next:
            return head

        i = head
        j = head.next
        while j:
            if j.val != i.val:
                i.next = j
                i = i.next
            j = j.next
        i.next = j

        return head
