from tombstone import Tombstone

class MemoryManagerSimulator:
    def __init__(self):
        self.symbol_table = {}

    def reserve(self, args):
        name, value = args

        if name in self.symbol_table:
            raise Exception(f"Cannot redeclare '{name}'")

        self.symbol_table[name] = Tombstone(value)

        return f"value '{value}' assigned to name '{name}'"

    def assign(self, args):
        name1, name2 = args

        if name2 not in self.symbol_table:
            raise Exception(f"'{name2}' is not defined")

        self.symbol_table[name1] = self.symbol_table[name2]

        return f"assigned '{name2}' to '{name1}'"

    def free(self, args):
        name, *_ = args

        if name not in self.symbol_table:
            raise Exception(f"'{name}' is not defined")
        
        self.symbol_table[name].free()

        return f"'{name}' freed"

    def print(self, args):
        name, *_ = args

        if name not in self.symbol_table:
            raise Exception(f"name '{name}' is not defined")
        
        val = self.symbol_table[name].value

        if val == None:
            raise Exception(f"name '{name}' points to an invalid pointer")

        return val
