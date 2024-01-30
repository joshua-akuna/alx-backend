#!/usr/bin/env python3

"""Defines the sub class FIFOCache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    You must use self.cache_data - dictionary from the parent
    class BaseCaching

        You can overload def __init__(self): but don’t forge
        to call the parent init: super().__init__()

        def put(self, key, item):
            Must assign to the dictionary self.cache_data the
            item value for the key key
            If key or item is None, this method should not do anything.
            If the number of items in self.cache_data is higher
            that BaseCaching.MAX_ITEMS:
                you must discard the first item put in cach
                (FIFO algorithm)
                you must print DISCARD: with the key discarded
                and following by a new line
        def get(self, key):
            Must return the value in self.cache_data linked to key
            If key is None or if the key doesn’t exist
            in self.cache_data, return None.
    """
    def __init__(self):
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """
        def put(self, key, item):
            Must assign to the dictionary self.cache_data the
            item value for the key key
            If key or item is None, this method should not do anything.
            If the number of items in self.cache_data is higher
            that BaseCaching.MAX_ITEMS:
                you must discard the first item put in cache
                (FIFO algorithm)
                you must print DISCARD: with the key discarded
                and following by a new line
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_list.append(key)
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                v = self.cache_list.pop(0)
                print("DISCARD: {}".format(v))
                self.cache_data.pop(v)

    def get(self, key):
        """
        def get(self, key):
            Must return the value in self.cache_data linked to key
            If key is None or if the key doesn’t exist
            in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
