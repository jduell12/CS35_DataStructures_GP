"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # left case?
        # check if the value is less than the root value?
        if value < self.value:
            # move to the left and check if it is none?
            if not self.left:
                # insert node here
                self.left = BSTNode(value)
            # otherwise
            else:
                # call insert on the root's left node
                self.left.insert(value)
        # right case?
        else:
        # otherwise
            # move to the right and check if it is none?
            if not self.right:
                # insert the node here
                self.right = BSTNode(value)
            # otherwise
            else:
                # call insert on the root's right node
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case?
        # check the root node value against target
        # if the root node's value and the target are the same
        if self.value == target:
            # return True
            return True 
        
        # left case
        # check if the target is less than the root's value
        if target < self.value:
            # check if there is no child to the left
            if not self.left:
                # return False
                return False 
            # otherwise
            else:
                # call contains on the left child
                return self.left.contains(target)
        # right case
        # otherwise
        else:
            # check if there is no child to the right
            if not self.right:
                # return False
                return False
            # otherwise
            else:
                # call contains on the right child
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        #base case 
        #tree is empty return None
        if not self:
            return None
        #while there is a right child 
        while self.right:
            #move to the right
            self = self.right
        
        #return the self's value once there are no more right children
        return self.value
    
    #Return the minimum value found in the tree
    def get_min(self):
        #base case 
        #tree is empty return None
        if not self:
            return None
        #while there is a left child
        while self.left:
            #move to the left
            self = self.left
        #return the self's value once there are no more left children
        return self.value
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #call for_each on the root 
        fn(self.value)
        #if left child exists then call for_each on left child
        if self.left:
            self.left.for_each(fn)
        #if right child exists then call for_each on right child
        if self.right:
            self.right.for_each(fn)
    

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    """
    queue
    grab starting node and put it in the queue
    if there are items in the queue 
        dequeue the current node
            mark it as visited
            print the node's value 
    check left 
        enqueue left
    check right 
        enqueue right 
    """
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
