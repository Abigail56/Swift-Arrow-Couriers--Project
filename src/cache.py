from collections import OrderedDict


class Cache:
    def __init__(self, size=10):
        self.size = size
        self.data = OrderedDict()

    def get(self, key):
        if key in self.data:
            value = self.data.pop(key)
            self.data[key] = value
            return value
        return None

    def put(self, key, value):
        if key in self.data:
            self.data.pop(key)
        elif len(self.data) >= self.size:
            self.data.popitem(last=False)
        self.data[key] = value

    def invalidate(self, key_prefix):
        for k in list(self.data.keys()):
            if k.startswith(key_prefix):
                del self.data[k]