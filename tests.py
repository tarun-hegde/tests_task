def filter_list(input_list):

    if len(input_list) % 10 != 0:
        raise ValueError("Input list must be a multiple of 10 in length.")

    return [item for i, item in enumerate(input_list) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]

# Get input from the user
while True:
    try:
        user_input = input("Enter a list of integers, separated by spaces: ")
        input_list = [int(x) for x in user_input.split()]
        filtered_list = filter_list(input_list)
        print("Filtered list:", filtered_list)
        break  # Exit the loop if input is valid
    except ValueError as e:
        print(e)


import unittest,random

class TestFilterList(unittest.TestCase):
    def test_valid_list(self):
        while True:
            try:
                user_input = input("Enter a valid list of integers (multiple of 10), separated by spaces: ")
                input_list = [int(x) for x in user_input.split()]
                expected_output = filter_list(input_list.copy())
                self.assertEqual(filter_list(input_list), expected_output)
                break
            except ValueError as e:
                print(e)

    def test_random_lists(self):
        for _ in range(10):
            list_length = random.randint(10, 100) * 10 
            input_list = random.sample(range(1, 101), list_length)
            expected_output = filter_list(input_list.copy())
            self.assertEqual(filter_list(input_list), expected_output)

    def test_invalid_list_length(self):
        with self.assertRaises(ValueError) as context:
            filter_list([1, 2, 3])
        self.assertEqual(str(context.exception), "Input list must be a multiple of 10 in length.")

    def test_empty_list(self):
        self.assertEqual(filter_list([]), [])

    def test_single_item_list(self):
        with self.assertRaises(ValueError) as context:
            filter_list([1])
        self.assertEqual(str(context.exception), "Input list must be a multiple of 10 in length.")

    def test_filtering_elements_at_positions_2_and_3(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = [1, 5, 7, 9]
        self.assertEqual(filter_list(input_list), expected_output)


if __name__ == '__main__':
    user_input_choice = input("Do you want to run tests (y/n)? ")
    if user_input_choice.lower() == 'y':
        unittest.main()
