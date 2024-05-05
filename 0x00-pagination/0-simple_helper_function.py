#!/usr/bin/env python3
""" index_range implementation """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns start index and end index """
    return ((page - 1) * page_size, page * page_size)
