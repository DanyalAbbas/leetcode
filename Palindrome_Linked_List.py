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


four = ListNode(1,None)
three = ListNode(2,four)
two = ListNode(2,three)
one = ListNode(1,two)

def foo(head : ListNode):
    temp = ""
    while head:
        temp += str(head.val)
        head = head.next
    if temp == temp[::-1]:
        return True
    return False

print(foo(one))
