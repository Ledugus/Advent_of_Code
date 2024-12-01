def create_files_day(number):
    f = open(f"2024/{number:02d}_input.txt", "w")
    f.close()
    f = open(f"2024/{number:02d}_test.txt", "w")
    f.close()
    f = open(f"2024/{number:02d}_solution.py", "w")
    f.write(
        f"""import numpy as np

def step_1(filename):
    f = open(filename)
    

    f.close()
    return 0
"""
    )
    f.write(
        f"""

def step_2(filename):
    f = open(filename)
    

    f.close()
    return 0
"""
    )
    f.write(f"\nprint(step_1('{number:02d}_test.txt'))\n")
    f.write(f"\nprint(step_2('{number:02d}_test.txt'))\n")
    f.close()


create_files_day(25)
