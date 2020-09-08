# lets code up a simple solution
"""
take 2 pointers lavel 1 'middle' and 1 to be 'end
start a loop putting both pointers at the initial node
while 'end' pointer is not None
increment the end pointer to the next node
if the end pointer is not None
increment the end pointer and increment the middler pointer to their next node respectively 
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def add(self, value):
        self.next = Node(value)
        
    def find_middle(self):
        middle = self
        end = self
        
        while end != None:
            end = end.next
            if end:
                end = end.next
                if end:
                    middle = middle.next
            
        print('Middle: %d' % (middle.value))
        
#odd number of values
#(4) -> (7) -> (9) -> (2) -> (12) 
# h             m             t

#even number of values
#(4) -> (7) -> (9) -> (2) -> (12) -> (120)
# h                m                   t
        
root = Node(4)
current_node = root
current_node.add(7)
current_node = current_node.next
current_node.add(9)
current_node = current_node.next
current_node.add(2)
current_node = current_node.next
current_node.add(12)
current_node = current_node.next
current_node.add(120)
root.find_middle()