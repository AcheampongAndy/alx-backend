#!/usr/bin/env python3
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """A FIFO caching system that inherits from BaseCaching.
    Items are discarded in a First-In-First-Out order when cache limit is reached.
    """

    def __init__(self):
        """Initialize the FIFOCache class with an order list for FIFO tracking."""
        super().__init__()
        self.order = []  # List to keep track of insertion order for FIFO

    def put(self, key, item):
        """Add an item to the cache using FIFO replacement policy."""
        if key is not None and item is not None:
            # Check if cache has reached its max capacity
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the first item added (FIFO)
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            # Add the new item to cache and record its order
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrieve an item by key from the cache."""
        return self.cache_data.get(key, None)
