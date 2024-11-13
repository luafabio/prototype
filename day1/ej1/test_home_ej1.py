import unittest
from home import read_file_to_array, find_pairs_with_sum

class TestHomeFunctions(unittest.TestCase):

    def test_read_file_to_array(self):
        # Create a temporary file for testing
        with open('test_input.txt', 'w') as f:
            f.write('1721\n979\n366\n299\n675\n1456\n')

        expected_array = [1721, 979, 366, 299, 675, 1456]
        result_array = read_file_to_array('test_input.txt')
        self.assertEqual(result_array, expected_array)

    def test_find_pairs_with_sum(self):
        my_array = [1721, 979, 366, 299, 675, 1456]
        target_sum = 2020
        expected_result = 514579  # 1721 * 299
        result = find_pairs_with_sum(my_array, target_sum)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
