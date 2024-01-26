#!/usr/bin/env python3
"""Defines the index_range function and the Server class"""

import csv
import math
from typing import List, Dict


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
        """
        Dataset indexed by starting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range (len(dataset))
            }
        return self.__indexed_dataset
    
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
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
        dataset = self.indexed_dataset()
        data_length = len(dataset)
        assert 0 <= index < data_length
        response = {}
        data = []
        response['index'] = index

        for i in range(page_size):
            while True:
                current = dataset.get(index)
                index += 1
                if current is not None:
                    break
            data.append(current)

        response['data'] = data
        response['page_size'] = len(data)

        if dataset.get(index):
            response['next_index'] = index
        else:
            response['next_index'] = None

        return response
