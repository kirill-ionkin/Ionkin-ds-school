# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen_before = set()
        while head is not None:
            if head in nodes_seen_before:
                return True
            nodes_seen_before.add(head)
            head = head.next
        return False
