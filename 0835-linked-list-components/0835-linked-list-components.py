# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)

        res = 0
        flag = False
        while head:
            if head.val not in num_set and flag:
                res += 1
                flag = False
            elif head.val in num_set:
                flag = True
            head = head.next

        if flag:
            res += 1

        return res 