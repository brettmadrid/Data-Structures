'''
  write a function that receive the head node of a linked list and an integer value 'k'.  
  Remove the kth node from the end of the linked list and return the head node of the new 
  linked list with the kth node from the end removed.
'''

# Simple Python3 program to find
# n'th node from end


class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # createNode and and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to get the nth node from
    # the last of a linked list
    def deleteKthFromLast(self, k):
        temp = self.head  # used temp variable
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1

        if (k < 0 or k > length):  # nothing to delete
            return self.head

        temp = self.head

        if k == length:  # remove head element
            self.head = temp.next
        else:
            for i in range(0, length-k-1):
                temp = temp.next

            nodeToDelete = temp.next
            temp.next = nodeToDelete.next
            nodeToDelete.next = None

        temp2 = self.head
        length2 = 0
        while temp2 is not None:
            print(temp2.data)
            temp2 = temp2.next
            length2 += 1
        print(length2)

        return self.head


# Driver Code
llist = LinkedList()
llist.push(11)
llist.push(12)
llist.push(13)
llist.push(14)
llist.push(15)
llist.push(16)
llist.push(17)
llist.push(18)
llist.push(19)
llist.push(20)
llist.deleteKthFromLast(10)
