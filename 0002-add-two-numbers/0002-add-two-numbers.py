# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        # print(curr.val)
        res = 0
        while l1 != None or l2 != None or res != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum_col = l1_val + l2_val + res
            # get result of sum (other digit except last one)
            res = sum_col // 10

            # get sum last digit         
            new_node = ListNode(sum_col % 10)
            curr.next = new_node
            curr = new_node
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next