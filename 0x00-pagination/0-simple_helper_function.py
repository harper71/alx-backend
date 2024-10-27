#!/usr/bin/env python3
"""return the index of the page"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns the start and end index if a api

    Args:
        page (int): current page number
        page_size (int): the number of items per page

    Returns:
        Tuple[int, int]: the start and end pages
    """

    start_index: int = (page - 1) * page_size
    end_index:int = start_index + page_size

    startNendIndex: Tuple[int, int] = (start_index, end_index)
    return startNendIndex
