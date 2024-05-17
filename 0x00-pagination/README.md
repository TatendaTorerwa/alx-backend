# Pagination

## Introduction
This project focuses on understanding and implementing pagination techniques for managing large datasets efficiently in web applications. By the end of this project, you'll grasp various pagination strategies and their implementation.

## Resources
Before diving into the tasks, make sure to review the following resources:
- [REST API Design: Pagination](https://www.youtube.com/watch?v=JTJ2WOiO9g4)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

## Learning Objectives
At the end of this project, you are expected to understand the following concepts without relying on external sources:
- Paginating datasets with simple parameters like page and page_size
- Implementing pagination with hypermedia metadata
- Achieving deletion-resilient pagination

## Requirements
- OS: Ubuntu 18.04 LTS
- Python Version: 3.7
- Coding Style: PEP 8
- All modules and functions should be properly documented and type-annotated.

## Setup: Popular_Baby_Names.csv
For this project, you'll be using the provided dataset file named `Popular_Baby_Names.csv`.

## Tasks
### 0. Simple Helper Function
Write a function `index_range` that calculates the start and end indexes for pagination based on the provided page and page_size parameters.

### 1. Simple Pagination
Implement the `Server` class with a method `get_page` to paginate the dataset. Ensure the method returns the correct page of data based on the given page number and page size.

### 2. Hypermedia Pagination
Enhance the `Server` class with a `get_hyper` method to provide hypermedia metadata along with the paginated data. The metadata should include information about the current page, total pages, next page, and previous page.

### 3. Deletion-Resilient Hypermedia Pagination
Modify the `Server` class to handle deletion-resilient pagination. Implement a method `get_hyper_index` that ensures users don't miss items from the dataset when rows are removed between queries.

## Conclusion
Pagination is a crucial aspect of web development, especially when dealing with large datasets. By completing these tasks, you'll gain practical experience in implementing various pagination techniques, ensuring efficient and user-friendly data navigation in your web applications. If you have any questions or encounter issues during the project, feel free to ask for assistance. Happy coding!

