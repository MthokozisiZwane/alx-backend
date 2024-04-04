#!/usr/bin/env python3
"""
 LFU Caching module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class
    """

    def __init__(self):
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Adds an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                keys_to_discard = [k for k, v in self.frequency.items()
                                   if v == min_freq]
                if len(keys_to_discard) > 1:
                    lru_key = min(self.cache_data, key=lambda k:
                                  self.cache_data[k])
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    print("DISCARD:", lru_key)
                else:
                    discard_key = keys_to_discard[0]
                    del self.cache_data[discard_key]
                    del self.frequency[discard_key]
                    print("DISCARD:", discard_key)

            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        """ Gets an item by key """
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
