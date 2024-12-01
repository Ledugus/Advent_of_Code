class Module:
    def __init__(self, outputs: list, inputs: list) -> None:
        self.outputs = outputs
        self.inputs = inputs

    def __str__(self) -> str:
        return " ".join(self.outputs)


class FlipFlop(Module):
    def __init__(self, name: str, outputs: list, inputs: list) -> None:
        super().__init__(outputs, inputs)
        self.name = name
        self.on = False

    def switch(self):
        self.on = not self.on

    def __str__(self) -> str:
        state = "ON" if self.on else "OFF"
        return f"{self.name} (FlipFlop) {state} -> " + super().__str__()


class Conjonction(Module):
    def __init__(self, name: str, outputs: list, inputs) -> None:
        super().__init__(outputs, inputs)
        self.name = name
        self.inputs: list[Module] = []

    def __str__(self) -> str:
        return f"{self.name} (Conjonction) {' '.join([module.state() for module in self.inputs])} -> " + super().__str__()


class BroadCaster(Module):
    def __str__(self) -> str:
        return "BroadCaster -> " + super().__str__()


def get_modules(filename):
    f = open(filename, "r")
    output_dict = {}
    input_dict = {}
    for line in f.readlines():
        type_and_name, outputs = line.strip().split(" -> ")
        outputs = outputs.split(", ")


def print_modules(modules_dict):
    print("MODULES STATES")
    for module in modules_dict.values():
        print(module)
    print()


def step_1(filename):
    modules_dict = get_modules(filename)
    print_modules(modules_dict)


print(step_1('20_test.txt'))
