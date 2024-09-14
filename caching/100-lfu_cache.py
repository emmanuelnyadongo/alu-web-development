#!/usr/bin/env python3
"""LFUCache that inherits from BaseCachin"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache """

    def __init__(self):
        """ Initialize LFU Cache """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        # If cache is full, discard the least frequency used item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
            if len(lfu_keys) > 1:
                lru_key = min(self.cache_data, key=self.cache_data.get)
                lfu_key = min(
                        lfu_keys,
                        key=lambda x: self.cache_data.get(x, 0))
                if lru_key in lfu_keys:
                    del self.cache_data[lru_key]
                    print(f"DISCARD: {lru_key}")
                else:
                    del self.cache_data[lfu_key]
                    print(f"DISCARD: {lfu_key}")
            else:
                lfu_key = lfu_keys[0]
                del self.cache_data[lfu_key]
                print(f"DISCARD: {lfu_key}")

            del self.frequency[lfu_key]

        self.cache_data[key] = item
        self.frequency[key] = 1

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Increment the frequency of the accessed key
        self.frequency[key] += 1
        return self.cache_data[key]
