import unittest
from home import read_file_to_array, exercise


class TestHomeFunctions(unittest.TestCase):

    def test_read_file_to_array(self):
        # Create a temporary file for testing
        with open('test_input.txt', 'w') as f:
            f.write('2-5 c: aaaaaaa\n1-3 b: cdefg\n2-9 c: ccccccccc\n')

        expected_array = [
            (2, 5, 'c', 'aaaaaaa'),
            (1, 3, 'b', 'cdefg'),
            (2, 9, 'c', 'ccccccccc')
        ]
        result_array = read_file_to_array('test_input.txt')
        self.assertEqual(result_array, expected_array)

    def test_exercise(self):
        my_array = [
            (15, 16, 'w', 'wwwwhwkwjnwwwwwdn') # 15-16 w: wwwwhwkwjnwwwwdn
        ]
        expected_result = 1  # Only the second password is valid
        result = exercise(my_array)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
