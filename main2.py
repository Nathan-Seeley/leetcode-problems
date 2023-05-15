# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):   
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         create dummy node to avoid any edge cases
#         set tail of list equal to dummy
#         Iterate through both lists with condition both are non-empty
#         Starting at the beginning of both lists compare the value from list one to list 2
#         insert the lesser of the two values into the output
#         then move to the next value
#         insert remaininder list into new list
#         """
#         dummy = ListNode()
#         tail = dummy

#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
#             tail = tail.next
#         if l1:
#             tail.next = l1
#         elif l2:
#             tail.next = l2
#         return dummy.next

# my_solution = Solution()
# result = my_solution.mergeTwoLists([1,2,4],[1,3,4])
# print (result)
