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
five = ListNode(5, None)
four = ListNode(4, five)
three = ListNode(3, None)
two = ListNode(2, three)
one = ListNode(1,two)


def foo(head : ListNode) -> ListNode:
    evenhead = None
    oddhead = None

    itr = head

    while itr:
        if not evenhead and itr.val%2==0:
            evenhead = itr
            evenhead.next = None
            smt1 = evenhead
            itr = itr.next
            continue
        elif not oddhead and itr.val%2:
            oddhead = itr
            oddhead.next = None
            smt2 = oddhead
            itr = itr.next
            continue
        
        evenhead.print()
        oddhead.print()
        if itr.val%2 == 0:
            smt1.next = itr
            smt1 = smt1.next
        else:
            smt2.next = itr
            smt2 = smt2.next
        itr = itr.next
    
foo(one)