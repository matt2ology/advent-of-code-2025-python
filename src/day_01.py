from src.base_day import BaseDay


class Day01(BaseDay):
    def __init__(self, data: list[str]):
        super().__init__(data)

    def part1(self) -> int:
        return len(self.data)

    def part2(self) -> int:
        return 0
