class Node:
    def __init__(self, key, val = 0):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # create the dummy nodes
        self.left, self.right = Node(0), Node(0)
        self.left.next, self.right.prev = self.right, self.left
    
    # helper: remove x node from list
    def remove(self, node):
        before, after = node.prev, node.next
        before.next = after
        after.prev = before
    # helper: add to the end of the list
    def insert(self, node):
        before, after = self.right.prev, self.right
        before.next = after.prev = node
        node.next, node.prev = after, before

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            # cache[key] is now a seperated node. still in the memory
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # first add, then check cap
        if key in self.cache:
            self.remove(self.cache[key])
        #update val, same key. create new Node if key doest exist
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            #delete from cache. importent
            del self.cache[lru.key]
