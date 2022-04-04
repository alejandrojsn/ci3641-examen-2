class Tombstone:
    def __init__(self, value):
        self.value = value
    
    def free(self):
        self.value = None
