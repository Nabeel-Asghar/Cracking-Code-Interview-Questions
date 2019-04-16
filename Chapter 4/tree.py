class Tree:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()

        print( self.data)

        if self.right:
            self.right.printTree()



    def insert(self,data):
        if self.data:
            if data<=self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)

            if data>=self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def findMiniumumElement(heap):

    n = len(heap)
    minimumElement = heap[0]

    for i in range(1, n):
        print( minimumElement)
        minimumElement = min(minimumElement, heap[i])

    return minimumElement

root = Tree(5)
root.insert(4)
root.insert(3)
root.insert(7)
root.insert(9)


heap = [20, 18, 10, 12, 8,
            9, 3, 5, 6, 8]

print(findMiniumumElement(heap))
