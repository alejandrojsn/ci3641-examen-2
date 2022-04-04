from functools import reduce

class Type:
    def __init__(self, name):
        self.name = name
    
    def size(self, packed_structs = False, packed_arrays = False):
        pass
    
    def alignment(self, packed_structs = False, packed_arrays = False):
        pass

    def waste(self, packed_structs = False, packed_arrays = False):
        pass

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


symbol_table = {}

def atomic_action(args):
    name, representation, alignment = args

    if name in symbol_table:
        raise Exception(f"Cannot redeclare {name}")
    
    if not representation.isnumeric():
        raise Exception(f"Representation must be a number")
    
    if not alignment.isnumeric():
        raise Exception(f"Alignment must be a number")
    
    symbol_table[name] = Atomic(name, int(representation), int(alignment))

def struct_action(args):
    name, *types = args

    if name in symbol_table:
        raise Exception(f"Cannot redeclare {name}")
    
    for type in types:
        if type not in symbol_table:
            raise Exception(f"Unknown type: {type}")
    
    symbol_table[name] = Struct(name, list(map(lambda t: symbol_table[t], types)))

def array_action(args):
    name, type, size = args

    if name in symbol_table:
        raise Exception(f"Cannot redeclare {name}")
    
    if type not in symbol_table:
        raise Exception(f"Unknown type: {type}")
    
    symbol_table[name] = Array(name, symbol_table[type], int(size))

def describe_action(args):
    name, *_ = args
    
    if name not in symbol_table:
        raise Exception(f"Unknown type: {name}")

    type = symbol_table[name]
    
    print(f"""
Tamaño (sin empaquetar): {type.size()}
Tamaño (empaquetando registros): {type.size(True)}
Tamaño (empaquetando arreglos): {type.size(False, True)}
Tamaño (empaquetado): {type.size(True, True)}
Alineación (sin empaquetar): {type.alignment()}
Alineación (empaquetando registros): {type.alignment(True)}
Alineación (empaquetando arreglos): {type.alignment(False, True)}
Alineación (empaquetado): {type.alignment(True, True)}
Bytes desperdiciados (sin empaquetar): {type.waste()}
Bytes desperdiciados (empaquetando registros): {type.waste(True)}
Bytes desperdiciados (empaquetando arreglos): {type.waste(False, True)}
Bytes desperdiciados (empaquetado): {type.waste(True, True)}
    """)


def exit_action(args):
    quit()

actions = {
    "ATOMICO": atomic_action,
    "STRUCT": struct_action,
    "ARREGLO": array_action,
    "DESCRIBIR": describe_action,
    "SALIR": exit_action
}

def run(input):
    action, *args = input.split(" ")

    try:
        actions[action](args)
    except KeyError:
        print(f"Unknown action: {action}")

if __name__ == "__main__":
    while True:
        run(input(">>> "))
