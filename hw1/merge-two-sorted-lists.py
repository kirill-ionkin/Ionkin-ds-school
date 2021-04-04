# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged_list = ListNode(0)
        current_elem = merged_list

        while l1 and l2:
            if l1.val > l2.val:
                current_elem.next = ListNode(l2.val)
                current_elem = current_elem.next
                l2 = l2.next

            elif l2.val > l1.val:
                current_elem.next = ListNode(l1.val)
                current_elem = current_elem.next
                l1 = l1.next

            elif l1.val == l2.val:
                current_elem.next = ListNode(l1.val)
                current_elem = current_elem.next
                current_elem.next = ListNode(l2.val)
                current_elem = current_elem.next
                l1 = l1.next
                l2 = l2.next

        while l1:
            current_elem.next = ListNode(l1.val)
            current_elem = current_elem.next
            l1 = l1.next

        while l2:
            current_elem.next = ListNode(l2.val)
            current_elem = current_elem.next
            l2 = l2.next

        return merged_list.next
