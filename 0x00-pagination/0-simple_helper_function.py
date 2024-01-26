#!/usr/bin/env python3
"""Defines the index_range function"""


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
