# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/


def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        value = self.map[key]
        self.map.pop(key)
        self.map[key] = value
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map.pop(key)
        if len(self.map)==self.capacity:
            #trick to get first val of a dict
            self.map.pop(next(iter(self.map)))
        self.map[key] = value
        return


#leetcode solution
def __init__(self, capacity: int):
        self.dict = OrderedDict()

        self.capacity = capacity

def get(self, key: int) -> int:
    if key not in self.dict:
        return -1
    else:
        self.dict.move_to_end(key)
        return self.dict[key]

def put(self, key: int, value: int) -> None:

    self.dict[key] = value
    self.dict.move_to_end(key)
    if len(self.dict)>self.capacity:
        self.dict.popitem(last = False)


