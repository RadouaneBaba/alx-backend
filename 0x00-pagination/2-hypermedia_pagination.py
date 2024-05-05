#!/usr/bin/env python3
""" index_range implementation """
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns start index and end index """
    return ((page - 1) * page_size, page * page_size)


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
        """ get page from dataset """
        self.dataset()
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        data_range = index_range(page, page_size)
        if (data_range[1] > len(self.__dataset)):
            return []
        return self.__dataset[data_range[0]:data_range[1]]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ get hyper implementation """
        hyper_data = self.get_page(page, page_size)
        cond = (page + 1) * page_size > len(hyper_data)
        return {
            "page_size": len(hyper_data),
            "page": page,
            "data": hyper_data,
            "next_page": page + 1 if cond else None,
            "prev_page": page - 1 if page >= 1 else None,
            "total_pages": len(hyper_data) / page_size
        }
