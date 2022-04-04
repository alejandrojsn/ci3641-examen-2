from type import Type

class Array(Type):
    def __init__(self, name, type, length):
        super().__init__(name)
        self.type = type
        self.length = length
    
    def size(self, packed_structs = False, packed_arrays = False):
        acc = 0
        alignment = self.type.alignment(packed_structs, packed_arrays)
        for i in range(self.length):
            padding = 0 if packed_arrays else (alignment - acc % alignment) % alignment

            acc += self.type.size(packed_structs, packed_arrays) + padding
        
        return acc
    
    def alignment(self, packed_structs = False, packed_arrays = False):
        if packed_arrays:
            return 1
        
        return self.type.alignment(packed_structs, packed_arrays)
    
    def waste(self, packed_structs = False, packed_arrays = False):
        if (packed_arrays):
            return 0

        type_waste = self.type.waste(packed_structs, packed_arrays)
        
        return self.size() - self.type.size() * self.length + type_waste * self.length
