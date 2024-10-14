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

three1 = ListNode(4, None)
two1 = ListNode(2, three1)
one1 = ListNode(1,two1)

three2 = ListNode(4, None)
two2 = ListNode(3, three2)
one2 = ListNode(1,two2)


def foo(l1 : ListNode, l2 : ListNode) -> ListNode:
    val = []
    while l1 or l2:
        val.append(l1.val)
        val.append(l2.val)
        l1 = l1.next
        l2 = l2.next
    
    head = None
    val = sorted(val)
    while val:
        if head is None:
            head = ListNode(val.pop(0), None)
        else:
            itr = head
            while itr.next:
                itr = itr.next
            itr.next = ListNode(val.pop(0), None)
    return head


print(foo(one1, one2))
foo(one1, one2).print()
