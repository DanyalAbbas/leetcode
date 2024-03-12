class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        if self.val is None:
            print("Linked list is empty")
            return
        llstr = ''
        while self:
            llstr += str(self.val)+' --> ' if self.next else str(self.val)
            self = self.next
        print(llstr)

five= ListNode(5, None)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1,two)


def foo(head : ListNode):
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev.print()
one.print()
foo(one)

def recursive(head : ListNode):
    if not head:
        return None
    
    nhead = head
    if head.next:
        nhead = recursive(head.next)
        head.next.next = head
    head.next = None
    return nhead





