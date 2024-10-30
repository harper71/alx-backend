#!/usr/bin/env python3
"""creating a caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """implementing the fist in first out system

    Args:
        BaseCaching (class): has all needed sata
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """puts data into the caching system

        Args:
            key (str): the key of data been stored
            item (Optional[Union[str, int, List, Tuple, Dict, set]]):all
            data that can be stored
        """

        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}")

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
