#!/usr/bin/env python3

"""
Create a class LIFOCache that inherits from BaseCachin
and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Create a class LIFOCache that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """
        You must use self.cache_data - dictionary
        from the parent class BaseCaching.
        You can overload def __init__(self): but don’t forget
        to call the parent init: super().__init__().
        """
        super().__init__()
        self.cache_list = []

    def put(self, k, v):
        """
        def put(self, key, item):
        Must assign to the dictionary self.cache_data the
        item value for the key key.
        If key or item is None, this method should not do anything.

        If the number of items in self.cache_data is higher
        that BaseCaching.MAX_ITEMS:
            you must discard the last item put in cache (LIFO algorithm)
            you must print DISCARD: with the key discarded and
            following by a new line
        """
        if k is not None or v is not None:
            self.cache_data[k] = v
            self.cache_list.append(k)
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                item = self.cache_list.pop(-2)
                print("DISCARD: {}".format(item))
                self.cache_data.pop(item)

    def get(self, k):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None.
        """
        return self.cache_data.get(k, None)
