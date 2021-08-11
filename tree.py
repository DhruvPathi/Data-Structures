class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []

    def addChild(self, node):
        node.parent = self
        self.children.append(node)
    
    def printTree(self):
        tab = '\t' * self.getLevel() + '|__' if self.parent else ''
        print(tab, self.data)
        for child in self.children:
            child.printTree()

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level

root = TreeNode("Electronics")

laptop = TreeNode("Laptop")
laptop.addChild(TreeNode("Mac"))
laptop.addChild(TreeNode("Surface"))
laptop.addChild(TreeNode("Thinkpad"))

cellphone = TreeNode("Cell Phone")
cellphone.addChild(TreeNode("iPhone"))
cellphone.addChild(TreeNode("Google Pixel"))
cellphone.addChild(TreeNode("Vivo"))

tv = TreeNode("TV")
tv.addChild(TreeNode("Samsung"))
tv.addChild(TreeNode("LG"))

root.addChild(laptop)
root.addChild(cellphone)
root.addChild(tv)

root.printTree()
