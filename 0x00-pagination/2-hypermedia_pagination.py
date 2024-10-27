#!/usr/bin/env python3
"""get pages"""
import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets the exact page requested

        Args:
            page (int, optional): current page number. Defaults to 1.
            page_size (int, optional): number of items page. Defaults to 10.

        Returns:
            List[List]: list of all the data gotten
        """

        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0, f"{page} must be greater than zero"
        assert page_size > 0, f"{page_size} must greater than Zero"
        correctedPages = index_range(page, page_size)

        if self.dataset() is None:
            return []

        return self.__dataset[correctedPages[0]:correctedPages[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        total_items: int = len(self.dataset())
        total_pages: int = (total_items + page_size - 1) // page_size
        data: List = self.get_page(page, page_size)

        data_objects = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_pages': page + 1 if page < total_pages else None,
            'previous_page': page - 1 if page > 1 else None,
            'total_pages': total_pages,
        }
        return data_objects
