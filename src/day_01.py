from src.base_day import BaseDay
from src.io import load_input_file


class Day01(BaseDay):
    def __init__(self, data: list[str], starting_position: int = 50):
        super().__init__(data)
        self.starting_position = int(starting_position)
        self.divisor: int = 100

    def part1(self) -> int:
        """`count_zero_landings`
        Simulate a sequence of dial rotations and count how many times the dial
        points to position **0**.

        Starting from `self.starting_position`, each movement instruction in
        `self.data` is processed to update the dial position. After every
        movement, the counter is incremented whenever the resulting position
        is **0**.

        Returns:
            int: The total number of times the dial points to position **0**
            during the simulation.
        """
        zero_counter: int = 0
        position: int = self.starting_position
        self.logging.info(f"The dial starts by pointing at {position}")
        for combination in self.data:
            combination_direction: str = combination[0].lower()
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
            zero_counter = self._increment_zero_counter(position, zero_counter)

            self.logging.info(
                f"The dial is rotated {combination} to point at {position}")

        return zero_counter

    def _increment_zero_counter(self, position: int, zero_counter: int) -> int:
        if position == 0:
            zero_counter += 1
        return zero_counter

    def _combination_movement_left(
            self, position, combination_direction, movement
    ) -> int:
        if combination_direction == "l":
            position = ((position + (-(movement))) % self.divisor)
        return position

    def _combination_movement_right(
            self, position, combination_direction, movement
    ) -> int:
        if combination_direction == "r":
            position = ((position + (movement)) % self.divisor)
        return position

    def part2(self) -> int:
        raise NotImplementedError("Part 2 not implemented yet")


if __name__ == "__main__":
    _data: list[str] = load_input_file("../input/day01_input.txt")
    print(Day01(_data).part1())
