import csv
from typing import List, Dict


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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        The goal here is that if between two queries,
        certain rows are removed from the dataset, the user
        does not miss items from dataset when changing page.
        Args:
            index (int): start index of the current page
            page_size (int): size of items required in current page
        Returns:
            Dict[int, int|List[List]|None]: a dict of the following:
                * index, next_index, page_size, data
        """

        assert isinstance(index, int)
        assert isinstance(page_size, int)
        assert index >= 0
        assert index < len(self.indexed_dataset())

        CSV = self.indexed_dataset()
        data = []

        next_index = index

        for _ in range(page_size):
            while not CSV.get(next_index):
                next_index += 1
            data.append(CSV.get(next_index))
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
