def try_race(try_time, max_time):
    return try_time * (max_time-try_time)


def step_1(filename):
    total = 1
    file = open(filename)
    times = list(map(int, file.readline().split(": ")[1].strip().split()))
    distances = list(map(int, file.readline().split(": ")[1].strip().split()))
    races = zip(times, distances)
    for race in races:
        count = 0
        time_max, distance_max = race
        for try_time in range(1, time_max):
            if try_race(try_time, time_max) > distance_max:
                count += 1
        total = total * count
    return total


def step_2(filename):
    file = open(filename)
    max_time = int("".join(file.readline().split(": ")[1].strip().split()))
    distance = int("".join(file.readline().split(": ")[1].strip().split()))
    current_time = 1
    while try_race(current_time, max_time) < distance:
        current_time += 1

    least_time = current_time
    current_time = max_time
    while try_race(current_time, max_time) < distance:
        current_time -= 1
    return current_time - least_time + 1


print(step_2("6_input.txt"))
