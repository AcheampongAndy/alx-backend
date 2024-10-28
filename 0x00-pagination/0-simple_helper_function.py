#!/usr/bin/env python3
"""
    Calculate the start and end index for a specific page in pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
     """
    Calculate the start and end index for a specific page in pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index.
    """
     return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
