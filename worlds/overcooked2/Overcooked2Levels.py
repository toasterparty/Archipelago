from enum import Enum


class Overcooked2World(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    KEVIN = 7

    def as_str(self) -> str:
        if self == Overcooked2World.KEVIN:
            return "Kevin"

        return str(int(self.value))

    def get_sublevel_count(self) -> int:
        if self == Overcooked2World.KEVIN:
            return 8

        return 6

    def get_base_id(self) -> int:
        if self == Overcooked2World.ONE:
            return 1

        prev = Overcooked2World(self.value - 1)
        return prev.get_base_id() + prev.get_sublevel_count()

    def name(self) -> str:
        if self == Overcooked2World.KEVIN:
            return "Kevin"

        return "World " + self.as_str()


class Overcooked2Level:
    world: Overcooked2World
    sublevel: int

    def __init__(self, world: Overcooked2World, sublevel: int):
        self.world = world
        self.sublevel = sublevel

    def __init__(self):
        self.world = Overcooked2World.ONE
        self.sublevel = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.sublevel += 1
        if self.sublevel > self.world.get_sublevel_count():
            if self.world == Overcooked2World.KEVIN:
                raise StopIteration
            self.world = Overcooked2World(self.world.value + 1)
            self.sublevel = 1

        return self

    def level_id(self) -> int:
        return self.world.get_base_id() + (self.sublevel - 1)

    def level_name(self) -> str:
        return self.world.as_str() + "-" + str(self.sublevel)

    def location_id_one_star(self) -> int:
        return 1000 + self.level_id()

    def location_id_two_star(self) -> int:
        return 2000 + self.level_id()

    def location_id_three_star(self) -> int:
        return 3000 + self.level_id()

    def location_name_one_star(self) -> str:
        return self.level_name() + " Reward (1-Star)"

    def location_name_two_star(self) -> str:
        return self.level_name() + " Reward (2-Star)"

    def location_name_three_star(self) -> str:
        return self.level_name() + " Reward (3-Star)"

    def world_name(self) -> str:
        return self.world.name()