from src.day_01 import Day01


class TestDay01:

    def setup_method(self):
        self.test_file = "day01_test.txt"

    def test_part1(self, load_input_file_fixture):
        data = load_input_file_fixture(self.test_file)
        assert Day01(data).part1() == 3
