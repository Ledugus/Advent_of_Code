def parse_file(filename):
    f = open(filename)
    line = f.readline().strip()
    workflows = {}
    parts = []
    while line:
        name, rules = line.strip("}").split("{")
        rules = rules.split(",")
        workflows[name] = rules
        line = f.readline().strip()
    line = f.readline().strip("\n{}")
    while line:
        values = line.split(',')
        values = {value.split("=")[0]: int(value.split("=")[1])
                  for value in values}
        parts.append(values)
        line = f.readline().strip("\n{}")
    return workflows, parts


def respects_condition(part_values: dict, condition_str):
    if condition_str[1] == ">":
        return part_values[condition_str[0]] > int(condition_str.split(">")[1])
    else:
        return part_values[condition_str[0]] < int(condition_str.split("<")[1])


def get_new_workflow(part_values: dict, current_workflow):
    for rule in current_workflow:
        split_rule = rule.split(":")
        print(split_rule)
        if len(split_rule) == 1:
            return rule
        if respects_condition(part_values, split_rule[0]):
            return split_rule[1]
    print("PAS DE NOUVEAU WORKFLOW TROUVE")
    return 'R'


def step_1(filename):
    total = 0
    workflows, parts = parse_file(filename)
    for part in parts:
        print("Current part : ", list(part.values()))
        part_total_value = sum(part.values())
        current_workflow = 'in'
        while current_workflow != 'A':
            print("Current workflow", current_workflow)
            if current_workflow == 'R':
                part_total_value = 0
                break
            current_workflow = get_new_workflow(
                part, workflows[current_workflow])

        total += part_total_value
        print()
    return total


print(respects_condition({'x': 100}, 'x>50'))
print(step_1('19_input.txt'))
