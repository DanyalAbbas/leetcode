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

l1 = [2,4,3]
l2 = [5,6,4]

three1 = ListNode(3, None)
two1 = ListNode(4, three1)
one1 = ListNode(2,two1)

three2 = ListNode(4, None)
two2 = ListNode(6, three2)
one2 = ListNode(5,two2)

def foo(l1 : ListNode, l2 : ListNode) -> ListNode:
    temp1, temp2 = "", ""
    while l1:
        temp1 += str(l1.val)
        l1 = l1.next
    while l2:
        temp2 += str(l2.val)
        l2 = l2.next
    
    added_val = int(temp1[::-1]) + int(temp2[::-1])
    added_val = list(str(added_val))

    head = None
    while added_val:
        if head is None:
            head = ListNode(added_val.pop(), None)
        else:
            itr = head

            while itr.next:
                itr = itr.next

            itr.next = ListNode(added_val.pop(), None)

    return head


print(foo(one1, one2))

foo(one1, one2).print()
