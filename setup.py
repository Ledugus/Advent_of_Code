def create_files_day(number):
    f = open(f"{number}_input.txt", "w")
    f.close()
    f = open(f"{number}_test.txt", "w")
    f.close()
    f = open(f"{number}_solution.py", "w")
    f.write("def step_1(filename):\n    f = open(filename)")
    f.write("\n")
    f.write(f"print(step_1('{number}_test.txt'))")
    f.close()


create_files_day(25)
