class Ship:
    def __init__(self, name, length, max_speed):
        self.name = name
        self.length = length
        self.max_speed = max_speed

    def get_info(self):
        return f"{self.name}, {self.length}, {self.max_speed}"


class Frigate(Ship):
    def __init__(self, name, length, max_speed, num_missiles):
        super().__init__(name, length, max_speed)
        self.num_missiles = num_missiles

    def fire_missile(self):
        return f"fires {self.num_missiles}"


class Destroyer(Ship):
    def __init__(self, name, length, max_speed, num_cannons):
        super().__init__(name, length, max_speed)
        self.num_cannons = num_cannons

    def fire_cannons(self):
        return f"fires {self.num_cannons}"

class Cruiser(Ship):
    def __init__(self, name, length, max_speed, num_aircraft):
        super().__init__(name, length, max_speed)
        self.num_aircraft = num_aircraft

    def launch_aircraft(self):
        return f"launches {self.num_aircraft}"

frigate = Frigate("frigate", 140, 50, 35)
print(frigate.get_info())
print(frigate.fire_missile())
destroyer = Destroyer("destroy", 170, 40, 50)
print(destroyer.get_info())
print(destroyer.fire_cannons())

cruiser = Cruiser("cruiser", 230, 55, 25)
print(cruiser.get_info())
print(cruiser.launch_aircraft())