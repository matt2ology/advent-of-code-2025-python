from src.day_01 import Day01


class TestDay01:

    def setup_method(self):
        self.day01_input = "day01_input.txt"
        self.day01_input_sample = "day01_input_sample.txt"

    def test_part1_sample(self, load_input_file_fixture):
        data = load_input_file_fixture(self.day01_input_sample)
        assert Day01(data).part1() == 3
