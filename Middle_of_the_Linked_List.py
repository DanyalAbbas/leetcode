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


two = ListNode(2, None)
one = ListNode(1,two)

def foo(head: ListNode):
    slow , fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


one.print()
foo(one).print()