"""
141. Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos
which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.
"""


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s_1 = s_2 = head
        while s_2 and s_2.next:
            s_1 = s_1.next
            s_2 = s_2.next.next
            if s_1 == s_2:
                return True
        return False


def main():
    sol = Solution()


if __name__ == "__main__":
    main()