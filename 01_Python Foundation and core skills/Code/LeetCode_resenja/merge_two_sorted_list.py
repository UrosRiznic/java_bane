class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> list:
        curr = dummy = ListNode()
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next

        if not l1:
            curr.next = l2
        else:
            curr.next = l1

        return dummy.next

solution = Solution()
l1 = [1,2,4]
l2 = [1,3,4]
print(solution.mergeTwoLists(l1, l2))