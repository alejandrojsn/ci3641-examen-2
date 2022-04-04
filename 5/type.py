class Type:
    def __init__(self, name):
        self.name = name
    
    def size(self, packed_structs = False, packed_arrays = False):
        pass
    
    def alignment(self, packed_structs = False, packed_arrays = False):
        pass

    def waste(self, packed_structs = False, packed_arrays = False):
        pass
