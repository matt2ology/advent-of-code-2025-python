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
    data = load_input_file("day01.txt")
    print(Day01(data).part1())
