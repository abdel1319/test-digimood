import random
from enum import Enum
from typing import Tuple


class Vessel:
    def __init__(self, coordinates: Tuple):
        self.coordinates = coordinates


class SupportCraft(Vessel):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.medical_unit = True


class OffensiveCraft(Vessel):
    def __init__(self, coordinates):
        super().__init__(coordinates)


class Craft(OffensiveCraft):
    def __int__(self, coordinates):
        super().__init__(coordinates)


class Refueling(OffensiveCraft):
    def __int__(self, coordinates):
        super().__init__(coordinates)


class Mechanical(OffensiveCraft):
    def __int__(self, coordinates):
        super().__init__(coordinates)


class Assitance(OffensiveCraft):
    def __int__(self, coordinates):
        super().__init__(coordinates)
        self.medical_unit = True


class Battleship(OffensiveCraft):
    def __int__(self, coordinates, attack_command):
        super().__init__(coordinates)
        self.attack_command = attack_command
        self.nb_cannons = 24


class AttackType(Enum):
    FIRE = "Fire"
    RAISE = "Raise shields"


class Cruiser(OffensiveCraft):
    def __int__(self, coordinates, attack_command):
        super().__init__(coordinates)
        self.attack_command = attack_command
        self.nb_cannons = 12


class Destroyer(OffensiveCraft):
    def __int__(self, coordinates, attack_command):
        super().__init__(coordinates)
        self.attack_command = attack_command
        self.nb_cannons = 6


class CommandShip(Battleship):
    def __init__(self, coordinates):
        super().__init__(coordinates)


grid = [[0] * 100 for _ in range(100)]

fleet = []

for _ in range(25):
    condition = True
    while condition:
        x, y = random.randint(0, 99), random.randint(0, 99)
        condition = grid[x][y] != 0
    fleet.append(OffensiveCraft((x, y)))
    grid[y][x] = 'O'

for _ in range(25):
    condition = True
    while condition:
        x, y = random.randint(0, 99), random.randint(0, 99)
        condition = grid[x][y] != 0
    fleet.append(SupportCraft((x, y)))
    grid[y][x] = 'S'


def find_positions(x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 100 and 0 <= new_y < 100 and grid[new_y][new_x] == 0:
            return new_x, new_y
    return None


pairs = []
for vessel in fleet:
    if isinstance(vessel, SupportCraft):
        adjacent_position = find_positions(vessel.coordinates[0], vessel.coordinates[1])
        if adjacent_position is not None:
            new_x, new_y = adjacent_position
            grid[vessel.coordinates[1]][vessel.coordinates[0]] = 'S'
            grid[new_y][new_x] = 'O'
            pairs.append((SupportCraft((x, y)), OffensiveCraft((x, y))))