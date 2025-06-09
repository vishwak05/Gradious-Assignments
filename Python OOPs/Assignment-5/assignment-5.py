# Node class for doubly linked list nodes used in LRUCache
class Node:
    def __init__(self, key, value):
        self.key = key      # Key for the cache
        self.value = value  # Value for the cache
        self.next = None    # Pointer to next node
        self.prev = None    # Pointer to previoud node

# LRUCache class implementing a fixed-size Least Recently Used cache
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()     # Dictionary for O(1) access to nodes by key
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # Remove a node from the doubly linked list
    def _remove(self, node:Node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
    
    # Add a node just before the tail (most recently used position)
    def _add(self, node:Node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
    
    # Retrieve value from cache and move node to most recently used position
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1   # Return -1 if not found in cache
    
    # Insert or update value in cache, evict least recently used if needed
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        # If over capacity, remove least recently used node (just after head)
        if len(self.cache) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]

# Decorator factory to apply LRU caching to function
def lru_cache_decorator(cache_size):
    cache = LRUCache(cache_size)
    def decorator(func):
        def wrapper(file_path):
            result = cache.get(file_path)
            # Result is -1 if file_path exists (cache hit)
            if result != -1:
                print(f"Cache hit for {file_path}")
                return result
            print(f"Cache miss for {file_path}")
            # Counting words if cache miss
            result = func(file_path)
            # Putting file_path and result in cache
            cache.put(file_path, result)
            return result
        return wrapper
    return decorator

# Decorate count_words with LRU cache of size 3
@lru_cache_decorator(3)
def count_words(file_path):
    try:
        with open(file_path, 'r') as f:
            text = f.read()
            # Split by whitespace to count words
            return len(text.split())
    except FileNotFoundError:
        print(f"File Not Found: {file_path}")
        return 0

# # Example usage:
print(count_words("a.txt"))     # Cache miss, reads file
print(count_words("b.txt"))     # Cache miss, reads file
print(count_words("a.txt"))     # Cache hit, returns cached result
print(count_words("c.txt"))     # Cache miss, reads file
print(count_words("d.txt"))     # Cache miss, evicts least recently used ('b.txt')