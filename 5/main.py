from array import Array
from atomic import Atomic
from struct import Struct

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
