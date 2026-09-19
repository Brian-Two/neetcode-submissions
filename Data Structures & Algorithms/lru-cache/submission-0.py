class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node
        
        self.left = Node(0, 0) #least recent used
        self.right =  Node(0,0) #most recent used

        self.left.next = self.right
        self.right.prev = self.left

    # remove from list
    def remove(self, node):
        # p c n 
            
        previous = node.prev
        nxt = node.next
        previous.next = nxt 
        nxt.prev = previous

    #insert at right
    def insert(self, node):
        previous, nxt = self.right.prev, self.right
        nxt.prev = node
        previous.next = node
        node.next = nxt
        node.prev = previous
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])

            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove the LRU cache: remove from the ist and delete from hash
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
