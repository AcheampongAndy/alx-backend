'''  FIFO caching
'''


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class `FIFOCache` that inherits from `BaseCaching`
       and is a caching system
    '''

    def __init__(self):
        ''' overload
        '''
        super().__init__()

    def put(self, key, item):
        '''  assign to the dictionary the item value for the key
        '''
        if key is not None and item is not None:
            if len(self.cache_data[key]) > BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(last=FALSE)
                print(f"DISCARD: {first_key}")

            self.cache_data[key] = item

    def get(self, key):
        ''' Retrieve an item by key from the cache.
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
