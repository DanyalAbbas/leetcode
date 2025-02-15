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

# six = ListNode(6, None)
# five = ListNode(5, None)
# four = ListNode(4, five)
# three = ListNode(3, None)
# two = ListNode(2, three)
one = ListNode(1,None)

def foo(head : ListNode, n : int) -> ListNode:
    FastTraversal = head
    SlowTraversal = head
    
    Fastcount = 1
    Slowcount = 0
    while FastTraversal.next and FastTraversal.next.next:
        # SlowTraversal = SlowTraversal.next
        # Slowcount += 1
        FastTraversal = FastTraversal.next.next
        Fastcount += 2
    Fastcount += 1 if FastTraversal.next else 0

    while Slowcount < Fastcount - n -1:
        SlowTraversal = SlowTraversal.next
        Slowcount += 1
    

    if Fastcount == n:
        head = head.next
        return head
        
    SlowTraversal.next = SlowTraversal.next.next
    
    return head

foo(one,1).print()

