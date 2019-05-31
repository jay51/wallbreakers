class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value
        self.prev = None
        self.next = None

        
class LRUCache:

    def __init__(self, capacity: int):
        self.hashtable = dict()
        self.total = 0
        self.capacity = capacity
        
        self.head = Node(None, None)
        self.head.prev = None
        
        self.tail = Node(None, None)
        self.tail.next = None
        '''
        head.next --> tail
        head    <--   tail.prev
        '''
        self.head.next = self.tail
        self.tail.prev = self.head
        
        
    def get(self, key: int) -> int:
        
        node = self.hashtable.get(key)        
        if not node:
            return -1
        
        # update the to the front of the list
        self.move_to_head(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        node = self.hashtable.get(key)
        if not node:
            # insert a new node to hashtable and doubly linked list
            node = Node(key, value)
            self.hashtable[key] = node
            self.add_node(node)
            self.total += 1
            
            if self.total > self.capacity:
                self.remove_LRUE()
                
        else:
            node.value = value
            self.move_to_head(node)


        
    def remove_LRUE(self):
        last = self.tail.prev
        self.remove_node(last)
        del self.hashtable[last.key]
        self.total -= 1
        
    
    def add_node(self, node):
        # update the head link
        node.prev = self.head
        node.next = self.head.next
        # update the prev node next to head to point to the new node next to head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        tmp_prev = node.prev
        tmp_next = node.next
        tmp_prev.next = tmp_next
        tmp_next.prev = tmp_prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)
        
