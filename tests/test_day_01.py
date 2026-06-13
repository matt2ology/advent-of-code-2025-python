from src.day_01 import Day01


class TestDay01:

    def setup_method(self):
        self.day01_input_sample_3_zero = "day01_input_sample_3_zero.txt"

    def test_part1_sample_3_zero(self, load_input_file_fixture):
        data = load_input_file_fixture(self.day01_input_sample_3_zero)
        assert Day01(data).part1() == 3
