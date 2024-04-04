#!/usr/bin/env python3
"""
 LRU Caching module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class
    """

    def __init__(self):
        super().__init__()
        self.lru_keys = []

    def put(self, key, item):
        """ Adds an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.lru_keys.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.lru_keys.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.lru_keys.append(key)

    def get(self, key):
        """ Gets an item by key """
        if key in self.cache_data:
            self.lru_keys.remove(key)
            self.lru_keys.append(key)
        return self.cache_data.get(key, None)
