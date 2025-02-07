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

seven = ListNode(6, None)
six = ListNode(2, seven)
five = ListNode(1, six)
four = ListNode(7, five)
three = ListNode(4, four)
two = ListNode(3, three)
one = ListNode(1,two)



def get_len(head : ListNode) -> int:
        itr = head
        length = 0
        while itr:
            itr = itr.next
            length += 1
        return length

def foo(head : ListNode) -> ListNode:
    n = get_len(head)//2
    count = 0
    itr = head
    while count < n -1:
        itr = itr.next
        count += 1
    itr.next = itr.next.next
    return head
 
    
one.print()
foo(one).print()

