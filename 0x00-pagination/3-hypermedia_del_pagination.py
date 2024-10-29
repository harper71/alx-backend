#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """Returns a dictionary with deletion-resilient pagination data."""
        assert index is not None and 0 <= index < len(self.indexed_dataset())

        data: List = []
        nxindex = index  # Track where we will continue after current page
        current_index = index  # Track current page index to start from

        # Loop to gather items up to page_size, skipping any missing items
        while len(data) < page_size and nxindex < len(self.indexed_dataset()):
            # Check if item exists in the indexed dataset
            if nxindex in self.indexed_dataset():
                data.append(self.indexed_dataset()[nxindex])
            # Move to the next index in sequence
            nxindex += 1

        return {
            "index": index,
            "next_index": nxindex,
            "page_size": len(data),
            "data": data
        }
