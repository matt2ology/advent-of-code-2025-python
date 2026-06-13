from src.base_day import BaseDay
from src.io import load_input_file


class Day01(BaseDay):
    def __init__(self, data: list[str]):
        super().__init__(data)

    def part1(self) -> int:
        zero_counter: int = 0
        position: int = 50
        for combination in self.data:
            combination_direction: str = combination[0]
            movement: int = int(combination[1:])
            position = self._combination_movement_left(
                position,
                combination_direction,
                movement
            )
            position = self._combination_movement_right(
                position,
                combination_direction,
                movement
            )
            zero_counter = self.incrament_zero_counter(position, zero_counter)

        return zero_counter

    def incrament_zero_counter(self, position: int, zero_counter: int) -> int:
        if position == 0:
            zero_counter += 1
        return zero_counter

    def _combination_movement_left(self, position, combination_direction, movement):
        if combination_direction.lower() == "l":
            position = ((position + (-(movement))) % 10)
        return position

    def _combination_movement_right(self, position, combination_direction, movement):
        if combination_direction.lower() == "r":
            position = ((position + (movement)) % 10)
        return position

    def part2(self) -> int:
        raise NotImplementedError("Part 2 not implemented yet")


if __name__ == "__main__":
    _data: list[str] = load_input_file("../input/day01_input_sample.txt")
    # _data: list[str] = load_input_file("../input/day01_input.txt")
    _zero_counter: int = 0
    _position: int = 50
    print("The dial starts by pointing", _position)
    for combination in _data:
        _combination_direction: str = combination[0]
        _movement: int = int(combination[1:])
        if _combination_direction.lower() == "l":
            _position = (_position - ((_movement))) % 10
            print(
                "\tThe dial is rotated", combination,
                "to point at", (_position + (_movement))
            )
        if _combination_direction.lower() == "r":
            _position = (_position + (_movement)) % 10
            print(
                "\tThe dial is rotated", combination,
                "to point at", (_position + (_movement))
            )
        if _position == 0:
            _zero_counter += 1
            print("\t+ Counter increased:", _zero_counter)
        print()

    print("COUNTER:", _zero_counter)
