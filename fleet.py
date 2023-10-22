from enum import Enum


class Vessel:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates


class SupportCraft(Vessel):
    def __init__(self, name, coordinates, support_type):
        super().__init__(name, coordinates)
        self.support_type = support_type
        self.medical_unit = True


class OffensiveCraft(Vessel):
    def __init__(self, name: str, coordinates):
        super().__init__(name, coordinates)


class Craft(OffensiveCraft):
    def __int__(self, name, coordinates):
        super().__init__(name, coordinates)
        self.medical_unit = True


class Reflueling(OffensiveCraft):
    def __int__(self, name, coordinates):
        super().__init__(name, coordinates)
        self.medical_unit = True


class Mechanical(OffensiveCraft):
    def __int__(self, name, coordinates):
        super().__init__(name, coordinates)
        self.medical_unit = True


class Assitance(OffensiveCraft):
    def __int__(self, name, coordinates):
        super().__init__(name, coordinates)
        self.medical_unit = True


class Battleship(OffensiveCraft):
    def __int__(self, name, coordinates, attack_command):
        super().__init__(name, coordinates)
        self.attack_command = attack_command
        self.nb_cannons = 24


class AttackType(Enum):
    FIRE = "Fire"
    RAISE = "Raise shields"


class Cruiser(OffensiveCraft):
    def __int__(self, name, coordinates, attack_command):
        super().__init__(name, coordinates)
        self.attack_command = attack_command
        self.nb_cannons = 12


class Destroyer(OffensiveCraft):
    def __int__(self, name, coordinates, attack_command):
        super().__init__(name, coordinates)
        self.attack_command = attack_command
        self.nb_cannons = 6


class CommandShip(Battleship):
    def __init__(self, name, coordinates, attack_command):
        super().__init__(name, coordinates, attack_command)


