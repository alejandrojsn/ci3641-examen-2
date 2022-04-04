from memory_manager_simulator import MemoryManagerSimulator
from runner import Runner

if __name__ == '__main__':
    runner = Runner(MemoryManagerSimulator())
    while True:
        print(runner.run(input(">>> ")))
