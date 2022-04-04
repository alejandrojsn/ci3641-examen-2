from type import Type

class Atomic(Type):
    def __init__(self, name, representation, alignment):
        super().__init__(name)
        self.representation = representation
        self._alignment = alignment
    
    def size(self, packed_structs = False, packed_arrays = False):
        return self.representation
    
    def alignment(self, packed_structs = False, packed_arrays = False):
        return self._alignment
    
    def waste(self, packed_structs=False, packed_arrays=False):
        return 0
