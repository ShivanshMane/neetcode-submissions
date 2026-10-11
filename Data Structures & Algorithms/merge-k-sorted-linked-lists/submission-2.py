# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
1) Understanding the problem 
   Input = array(k linked lists), sorted list(asc order)
   Task = Merge k linked list in asc order 
   Goal = return the merged linked list in 1 array 

2) Constraints = size of linked list, is linked list sorted, can the array be empty, can both the array and the linked list be empty 

3) Example = [[1,2,4],[1,3,5],[3,6]]
             []
             [[]]

4) Approach = Brute Force Solution = Merge two linked list first, and then merge the third one with the new merged(1 and 2)

'''

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                mergedLists.append(self.mergeTwoLists(l1, l2))

            lists = mergedLists

        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next 
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
        