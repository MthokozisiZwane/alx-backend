#!/usr/bin/env python3
"""
MRU Caching module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Adds an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
                print("DISCARD:", key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = next(iter(self.cache_data))
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Gets an item by key """
        if key in self.cache_data:
            del self.cache_data[key]
            self.cache_data[key] = key
        return self.cache_data.get(key, None)
