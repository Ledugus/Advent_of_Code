def create_files_day(number):
    f = open(f"2024/{number:02d}_input.txt", "w")
    f.close()
    f = open(f"2024/{number:02d}_test.txt", "w")
    f.close()
    f = open(f"2024/{number:02d}_solution.py", "w")
    f.write(
        """import numpy as np

def step_1(filename):
    f = open(filename)
    
    count = 0

    f.close()
    return count
"""
    )
    f.write(
        """

def step_2(filename):
    f = open(filename)
    
    count = 0

    f.close()
    return count
"""
    )
    f.write(f"\nprint(step_1('2024/{number:02d}_input.txt'))\n")
    f.write(f"\nprint(step_2('2024/{number:02d}_input.txt'))\n")
    f.close()


create_files_day(5)
