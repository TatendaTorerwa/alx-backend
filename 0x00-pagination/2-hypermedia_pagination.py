#!/usr/bin/env python3
"""
Add the class to read and store the dataset in a list of lists
and method to the class that will allow for
retrieving pages of data.
"""
import csv
import math
from typing import List, Tuple, Dict, Union


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
        """
        Get data for the given page number
        Args:
            age (int): page number
            page_size (int): number of items per page
        Returns:
            (List[List]): a list of list(row) if inputs are within range
            ([]) : an empty list if page and page_size are out of range
        """

        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        start_index, end_index = self.index_range(page, page_size)

        if (len(self.dataset()) < start_index or
                len(self.dataset()) < end_index):
            return []

        pagination_names = []
        for i in range(start_index, end_index):
            pagination_names.append(self.dataset()[i])
        return pagination_names

    def get_hyper(self, page: int = 1, page_size:
                  int = 10) -> Dict[str, Union[int, List[List], None]]:
        start_index, end_index = self.index_range(page, page_size)

        next_page = page + 1 if len(self.dataset()) > end_index else None

        prev_page = page - 1 if page > 1 else None

        totalRows = len(self.dataset())
        total_pages = totalRows // page_size
        if totalRows % page_size != 0:
            total_pages += 1

        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        Calculates start index and an end index corresponding to the range of
        indexes to return in a list for those particular pagination parameters.

        Args:
            page (int): the current page
            page_size (int): the amount of items in a page

        Returns:
            (tuple): a tuple of the start and end index for the given page
        """

        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return (start_index, end_index)
