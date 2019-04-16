class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current

    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next


    def delete(self, key):

        previous = None
        current = self.head

        while current:
            if current.data == key:
                if previous:
                    previous.next = current.next
                    return
                else:
                    self.head = current.next


            previous = current
            current = current.next

        return 0

    def kthelement(self, key):
        current = self.head
        size = self.size()
        kth = size - key

        #Iterate through linked list till you get to the kth element
        for i in range(kth):
            current = current.next

        #Return the kth element
        return(current.data)

    def size(self):
        current = self.head
        counter = 0

        #Iterate through the linked list to find the size of it
        while current:
            counter = counter+1
            current=current.next

        return counter

    def palindrome(self):

        current = self.head
        size = self.size()
        array = []
        index = 0

        while current:
            array.append(current.data)
            current = current.next

        for i in range(len(array)):
            if array[i] == array[size-i-1]:
                continue
            else:
                return

        print("This is a palindrome")


    def reverse(self):

        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

def duplicate(list):
    first = list.head

    while first:
        second = first.next

        while second:
            if first.data == second.data:
                l.remove(second)
            second = second.next

        first = first.next


l = LinkedList()
x = [1,2,3,4,5]

for i in x:
    l.insert(i)



l.reverse()
l.printList()
