#!/usr/bin/env python3

"""
Defines the sub class BasicCache
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    Implements a basic cache
    """
    def put(self, k, v):
        """
        puts a key value pair into the cache
        """
        self.cache_data[k] = v

    def get(self, k):
        """get a value from the cache based on the key arg
        """
        return self.cache_data.get(k)
