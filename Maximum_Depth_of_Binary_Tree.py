class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = TreeNode(data)




def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = TreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root




def foo(root : TreeNode) -> int:
    if not root:
        return 0
    countLeft, countRight = 0, 0

    countLeft += foo(root.left)
    countRight += foo(root.right)

    
    return 1 + max(countLeft, countRight)


if __name__ == "__main__":
    elements = [3,9,20,15,7]
    nl = build_tree(elements)
    print(foo(nl))