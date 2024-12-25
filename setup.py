def create_files_day(number):
    with open(f"2024/{number:02d}_input.txt", "w") as f:
        f.write("")
    with open(f"2024/{number:02d}_test.txt", "w") as f:
        f.write("")
    with open(f"2024/{number:02d}_solution.py", "w") as f:
        f.write(
            f"""import numpy as np
from time import time
from utils import *


def step_1(filename):
    exec_time = time()
    f = open(filename)
    
    count = 0

    f.close()

    print("Part 1 exec time :", time() - exec_time)
    return count


def step_2(filename):
    exec_time = time()
    f = open(filename)
    
    count = 0

    f.close()
    print("Part 2 exec time :", time() - exec_time)
    return count


print(step_1('2024/{number:02d}_test.txt'))
print(step_1('2024/{number:02d}_input.txt'))

print(step_2('2024/{number:02d}_test.txt'))
print(step_2('2024/{number:02d}_input.txt'))"""
        )


create_files_day(25)
