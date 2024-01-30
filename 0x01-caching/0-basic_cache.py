#!/usr/bin/env python3

"""
Defines the sub class BasicCache
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    Implements a basic cache
    """
    def put(self, key, item):
        """
        puts a key value pair into the cache
        """
        self.cache_data[key] = item

    def get(self, key):
        """get a value from the cache based on the key arg
        """
        return self.cache_data.get(key)
