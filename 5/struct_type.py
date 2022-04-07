from functools import reduce
from type import Type
import math

class StructType(Type):
    def __init__(self, name, types):
        super().__init__(name)
        self.types = types
    
    def size(self, packed_structs = False, packed_arrays = False):
        def reducer(acc, type):
            alignment = type.alignment(packed_structs, packed_arrays)

            padding = 0 if packed_structs else (alignment - acc % alignment) % alignment

            return acc + type.size(packed_structs, packed_arrays) + padding

        size = reduce(reducer, self.types, 0)
        
        return size
    
    def alignment(self, packed_structs=False, packed_arrays=False):
        if packed_structs:
            return 1
        
        return math.lcm(*map(lambda t: t.alignment(packed_structs, packed_arrays), self.types))
    
    def waste (self, packed_structs=False, packed_arrays=False):
        if (packed_structs):
            return sum(map(lambda t: t.waste(packed_structs, packed_arrays), self.types))
        
        return self.size() \
             - sum(map(lambda t: t.size(packed_structs, packed_arrays), self.types)) \
             + sum(map(lambda t: t.waste(packed_structs, packed_arrays), self.types))
