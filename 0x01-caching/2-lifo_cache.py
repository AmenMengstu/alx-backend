#!/usr/bin/python3
""" LIFOCache that inherits from BaseCaching and is a caching system
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - inherits from BaseCaching and is a caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the {} self.cache_data the item value for the key
        """
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                keys = list(self.cache_data.keys())
                print("DISCARD: {}".format(keys[-1]))
                del self.cache_data[keys[-1]]
                self.cache_data[key] = item

    def get(self, key):
        """return value in self.cache_data linked to key
        """
        if not key or not self.cache_data.get(key):
            return None
        return self.cache_data.get(key)
