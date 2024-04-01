#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict
Server = __import__('2-hypermedia_pagination').Server
index_range = __import__('0-simple_helper_function').index_range
# get_page = __import__('1-simple_pagination').get_page


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
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10):
        """Retrieve a page of dataset based on pagination parameters"""
        assert isinstance(page, int) and page > 0, "Page must be positive int"
        assert isinstance(page_size, int) and page_size > 0, "must be pos int"

        dataset = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieves hypermedia information for pagination with index"""
        assert index is None or (isinstance(index, int) and 0 <= index <
                                 len(self.dataset())), "Index out of range"
        assert isinstance(page_size, int) and page_size > 0, "must be +ve int"

        if index is None:
            page = 1
        else:
            page = index // page_size + 1

        data = self.get_page(page, page_size)
        next_index = (page * page_size) if len(data) == page_size else None

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
