#!/usr/bin/env python3
"""creating a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ a basic caching system

    Args:
        BaseCaching (dict): impements get and put methods in a caching
        system
    """
    def __init__(self):
        super().__init__()

    def put(self, key: str, item) -> None:
        """puts data into the caching system

        Args:
            key (str): the key of data been stored
            item (Optional[Union[str, int, List, Tuple, Dict, set]]):all
            data that can be stored
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

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
