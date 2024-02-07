from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detect_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    if not fast or not fast.next:
        return None
    fast = head
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return slow
