#!/usr/bin/env python3
"""Defines the index_range function and Server class"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """
    the function takes in two integers page and page_size and returns
    a tuple of size 2 containing a start index and an end index
    corresponding to the range of indexes to return in a list.
    """
    begin, end = 0, 0

    for i in range(page):
        begin = end
        end += page_size

    return (begin, end)


class Server:
    """
    Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Class constructor"""
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
        """
        the function uses the index_range function to find the correct
        indexes to paginate the dataset correctly and return the appropriate
        page of the dataset (i.e. the correct list of rows)
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page > 0

        dataset = self.dataset()
        data_length = len(dataset)

        try:
            index = index_range(page, page_size)
            return dataset[index[0]: index[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary containing the following key-value pairs:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page
            next_page: the number of the next page or None if no next page
            prev_page: the number of the previous page, or None if
                no previous page
            total_pages: the total number of pages in the dataset as an int
        """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        if page - 1 > 1 or page - 1 <= total_pages:
            prev_page = page - 1
        else:
            prev_page = None
        if page + 1 < 1 or page + 1 > total_pages:
            next_page = None
        else:
            next_page = page + 1
        hdict = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "prev_page": prev_page,
            "next_page": next_page,
            "total_pages": total_pages
        }
        return hdict
