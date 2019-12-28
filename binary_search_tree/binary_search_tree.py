# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if inserting we must already have a tree/root
        # if value is less than self.value go left
        if value < self.value:
            # make a new tree/node if empty
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # otherwise keep going (recursion)
                self.left.insert(value)

        # if greater than or equal to self.value, go right
        if value >= self.value:
            # make a new tree/node if empty
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                # otherwise keep going (recursion)
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        if target == self.value:
            return True
        # go left or right based on smaller or bigger
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        if self.right:
            return self.right.get_max()
        # otherwise return self.value
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # 1st Method Recursively
        # cb(self.value)
        # if self.left:
        #     self.left.for_each(cb)
        # if self.right:
        #     self.right.for_each(cb)

        # 2nd Method Iteratively
        stack = Stack()
        stack.push(self)  # push node onto the stack

        while stack.len():
            current_node = stack.pop()
            # add current_node's right and left children to the stack
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # recurses all the way left before starting to print
    # after left then recurses right, printing as it goes
    def in_order_print(self, node):
        if self.value:
            # Recurse left until at the final left node
            if self.left:
                self.left.in_order_print(self.left)

            # When recursed all the way left start printing
            # Then print values on the right on each recursive pass
            print(self.value)

            # Recurse right until at the end
            if self.right:
                self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if not node.value:
            return
        else:
            # create a queue
            queue = Queue()
            # enqueue first node onto the queue
            queue.enqueue(node)
            while queue.len():
                # dequeue node and print it
                current = queue.dequeue()
                print(current.value)

                # check to see of node has any children
                # if so, add them to the queue
                if current.left:
                    queue.enqueue(current.left)
                if current.right:
                    queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        if not node.value:
            return
        else:
            # create a stack
            stack = Stack()
            # push first node onto the stack
            stack.push(node)
            while stack.len():
                # pop node and print it
                current = stack.pop()
                print(current.value)

                # check to see of node has any children
                # if so, add them to the stack
                if current.left:
                    stack.push(current.left)

                if current.right:
                    stack.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if self.value:
            print(self.value)
            if self.left:
                self.left.pre_order_dft(self.left)
            if self.right:
                self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT

    def post_order_dft(self, node):
