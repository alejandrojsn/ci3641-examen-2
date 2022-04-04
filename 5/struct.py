from functools import reduce
from type import Type

class Struct(Type):
    def __init__(self, name, types):
        super().__init__(name)
        self.types = types
    
    def size(self, packed_structs = False, packed_arrays = False):
        def reducer(acc, type):
            alignment = type.alignment(packed_structs, packed_arrays)

            padding = 0 if packed_structs else alignment - acc % alignment

            return acc + type.size(packed_structs, packed_arrays) + padding

        size = reduce(reducer, self.types, 0)
        alignment = self.alignment(packed_structs, packed_arrays)
        aligned = size + alignment - size % alignment
        
        return size if packed_structs else aligned
    
    def alignment(self, packed_structs=False, packed_arrays=False):
        if packed_structs:
            return 1
        
        return max(map(lambda t: t.alignment(packed_structs, packed_arrays), self.types))
    
    def waste (self, packed_structs=False, packed_arrays=False):
        if (packed_structs):
            return 0
        
        return self.size() \
             - sum(map(lambda t: t.size(packed_structs, packed_arrays), self.types)) \
             + sum(map(lambda t: t.waste(packed_structs, packed_arrays), self.types))
