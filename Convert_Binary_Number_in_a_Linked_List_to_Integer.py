class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

three = ListNode(1,None)
two = ListNode(0,three)
one = ListNode(1,two)

def foo(head : ListNode):
    result = head.val
    while head.next != None:
        result = result*2 + head.next.val
        head = head.next
    return result

print(foo(one))