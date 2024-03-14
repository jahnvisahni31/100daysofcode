class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-node pairs
        self.head = ListNode()  # Dummy head node
        self.tail = ListNode()  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        # Add a node to the front of the linked list
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        # Remove a node from the linked list
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_front(self, node):
        # Move a node to the front of the linked list (most recently used position)
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        # Remove the node at the tail of the linked list (least recently used)
        tail = self.tail.prev
        self._remove_node(tail)
        return tail

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move the corresponding node to the front
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used node from the cache
                evicted_node = self._pop_tail()
                del self.cache[evicted_node.key]
            # Add the new node to the front
            new_node = ListNode(key, value)
            self._add_node(new_node)
            self.cache[key] = new_node

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
