#!/usr/bin/env python3
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """A basic caching system that inherits from BaseCaching.
    This system has no limit on cache size.
    """

    def put(self, key, item):
        """Add an item to the cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key from the cache."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
