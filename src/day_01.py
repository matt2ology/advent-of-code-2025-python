from .base_day import BaseDay


class Day01(BaseDay):
    def __init__(self, data: list[str]):
        super().__init__(data)

    def part1(self) -> int:
        return len(self.data)


if __name__ == "__main__":
    data = Day01.load_input_file("day01.txt")
    print(Day01(data).part1())
