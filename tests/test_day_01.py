from src.day_01 import Day01


class TestDay01:

    def setup_method(self):
        self.day01_input_sample_3_zero = "day01_input_sample_3_zero.txt"
        self.day01_input_sample_2_zero_start_11 = "day01_input_sample_2_zero_start_11.txt"
        self.day01_input_sample_1_zero_start_5 = "day01_input_sample_1_zero_start_5.txt"

    def test_part1_sample_3_zero(self, load_input_file_fixture):
        data = load_input_file_fixture(self.day01_input_sample_3_zero)
        assert Day01(data).part1() == 3

    def test_part1_sample_3_zero_start_11(self, load_input_file_fixture):
        """
        if the dial were pointing at `11`, a rotation of `R8`
        would cause the dial to point at `19`.
        After that, a rotation of `L19` would cause it to point at `0`.

        Because the dial is a circle, turning the dial **left from 0**
        one click makes it point at `99`. Similarly,
        turning the dial **right from 99** one click makes it point at `0`.
        """
        data = load_input_file_fixture(self.day01_input_sample_2_zero_start_11)
        assert Day01(data, 11).part1() == 2

    def test_part1_sample_1_zero_start_5(self, load_input_file_fixture):
        """
        if the dial were pointing at `5`, a rotation of `L10`
        would cause it to point at `95`. After that,
        a rotation of `R5` could cause it to point at `0`.
        """
        data = load_input_file_fixture(self.day01_input_sample_1_zero_start_5)
        assert Day01(data, 5).part1() == 1
