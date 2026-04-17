from src.day_01 import Day01
from src.io import load_input


def run_day_01():
    data = load_input("day01.txt")

    solver = Day01(data)

    print("Part 1:", solver.part1())
    print("Part 2:", solver.part2())


if __name__ == "__main__":
    run_day_01()
