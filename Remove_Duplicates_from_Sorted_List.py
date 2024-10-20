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

l1 = [1,1,2]

three1 = ListNode(2, None)
two1 = ListNode(1, three1)
one1 = ListNode(1,two1)

def foo(head : ListNode) -> ListNode:
    duplicated = []
    l = []
    while head:
        if head.val in duplicated:
            head = head.next
            continue
        l.append(head.val)
        duplicated.append(head.val)
        head = head.next
    
    l = sorted(l)

    head = None
    while l:
        if not head:
            head = ListNode(l[0], None)
            l.pop(0)
        else: 
            itr = head

            while itr.next:
                itr = itr.next
            
            itr.next = ListNode(l[0], None)
            l.pop(0)




    return head

print(foo(one1))
foo(one1).print()