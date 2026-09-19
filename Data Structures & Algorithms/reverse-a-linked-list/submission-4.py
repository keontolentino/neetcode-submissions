# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: #If head is empty
            return None
        
        newHead = head #Create another pointer moving forward
        if head.next: #If head.next is not None
            newHead = self.reverseList(head.next) #Set new head to next node repeatedly until value is None
            head.next.next = head #Return to the paused function call and set the pointer = original head to point to the nodes backward
        head.next = None # Break the pointer going forward and at the last call the value is None

        return newHead #Returns the node value after every call 
