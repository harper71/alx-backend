#!/usr/bin/env python3
"""
implements the lifo system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """implements a last in first out 
        caching system

        Args:
            key (str): key of data being added
            item (any): data been added
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the last key inserted (LIFO)
            last_key = next(reversed(self.cache_data))
            self.cache_data.pop(last_key)
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """get values of the asociated key

        Args:
            key (string): key to the data in the cache

        Returns:
            Any: value of the data
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
