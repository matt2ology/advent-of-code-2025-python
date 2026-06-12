from src.base_day import BaseDay
from src.io import load_input_file


class Day01(BaseDay):
    def __init__(self, data: list[str]):
        super().__init__(data)

    def part1(self) -> int:
        return len(self.data)

    def part2(self) -> int:
        raise NotImplementedError("Part 2 not implemented yet")


if __name__ == "__main__":
    _data: list[str] = load_input_file("../input/day01_input_sample.txt")
    _zero_counter: int = 0
    _position: int = 0
    for combination in _data:
        print("Combination:", combination)
        _combination_direction: str = combination[0]
        _movement: int = int(combination[1:])
        print("\tPrevious position:", _position)
        print("\tRotation:", _combination_direction, "Movement:", _movement)
        if _combination_direction.lower() == "l":
            _position = (_position + (-(_movement))) % 10
            print("\tMove LEFT by:", _position, "positions")
        if _combination_direction.lower() == "r":
            _position = (_position + (_movement)) % 10
            print("\tMove RIGHT by:", _position, "positions")
        if _position == 0:
            _zero_counter += 1
            print("\t+ Counter increased:", _zero_counter)
        print()

    print("COUNTER:", _zero_counter)
