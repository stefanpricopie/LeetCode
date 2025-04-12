# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        # Step 1: Extract values into a list
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next

        # Step 2: Sort the list
        vals.sort()

        # Step 3: Rebuild the linked list
        dummy = ListNode()
        current = dummy
        for val in vals:
            current.next = ListNode(val)
            current = current.next

        return dummy.next