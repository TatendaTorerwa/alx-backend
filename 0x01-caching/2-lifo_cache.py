#!/usr/bin/env/python3
""" LIFO Caching: Create a class LIFOCache that inherits from BaseCaching
                  and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ A LIFO Cache.
        Inherits all behaviors from BaseCaching except, upon any attempt to
        add an entry to the cache when it is at max capacity (as specified by
        BaseCaching.MAX_ITEMS), it discards the newest entry to accommodate for
        the new one.
        Attributes:
          __init__ - method that initializes class instance
          put - method that adds a key/value pair to cache
          get - method that retrieves a key/value pair from cache """

    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.stack = []

    def put(self, key, item):
      """ Add key/value pair to cache data.
            If cache is at max capacity (specified by BaseCaching.MAX_ITEMS),
            discard newest entry in cache to accommodate new entry. """
      if key is None or item is None:
            return

      if key in self.cache_data:
            self.stack.remove(key)

      self.cache_data[key] = item
      self.stack.append(key)

      if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Return value stored in `key` key of cache.
            If key is None or does not exist in cache, return None. """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
