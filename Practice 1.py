class Device:
    def __init__(self, name, brand, power_consumption):
        self.name = name
        self.brand = brand
        self.power_consumption = power_consumption

    def get_info(self):
        return f"{self.name},{self.brand},{self.power_consumption}"


class CoffeeMachine(Device):
    def __init__(self, name, brand, power_consumption, coffee_type):
        super().__init__(name, brand, power_consumption)
        self.coffee_type = coffee_type

    def make_coffee(self):
        return f"makes {self.coffee_type}"


class Blender(Device):
    def __init__(self, name, brand, power_consumption, speed_levels):
        super().__init__(name, brand, power_consumption)
        self.speed_levels = speed_levels

    def blend(self):
        return "blends"


class MeatGrinder(Device):
    def __init__(self, name, brand, power_consumption, capacity):
        super().__init__(name, brand, power_consumption)
        self.capacity = capacity

    def grind_meat(self):
        return "grinding meat"

coffee_machine = CoffeeMachine("AP1000", "Redmond", 1200, "латте")
print(coffee_machine.get_info())
print(coffee_machine.make_coffee())
blender = Blender("F100", "Starbucks", 1100, 4)
print(blender.get_info())
print(blender.blend())
meat_grinder = MeatGrinder("WQ210", "Bork", 1200, "1.5kg")
print(meat_grinder.get_info())
print(meat_grinder.grind_meat())