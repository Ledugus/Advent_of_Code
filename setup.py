def create_files_day(number):
    with open(f"2024/{number:02d}_input.txt", "w") as f:
        f.write("")
    with open(f"2024/{number:02d}_test.txt", "w") as f:
        f.write("")
    with open(f"2024/{number:02d}_solution.py", "w") as f:
        f.write(
            f"""import numpy as np
from utils import *

def step_1(filename):
    f = open(filename)
    
    count = 0

    f.close()
    return count


def step_2(filename):
    f = open(filename)
    
    count = 0

    f.close()
    return count


print(step_1('2024/{number:02d}_test.txt'))
print(step_1('2024/{number:02d}_input.txt'))

print(step_2('2024/{number:02d}_test.txt'))
print(step_2('2024/{number:02d}_input.txt'))"""
        )


create_files_day(19)
