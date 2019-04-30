import unittest
from Sorts import bubble_sort, merge_sort, quick_sort

class TestSorts(unittest.TestCase):
    
    def test_bubble_sort(self):
        unsorted_arr = [6, 9, 7, 2, 3, 6, 5]
        sorted_arr = [2, 3, 5, 6, 6, 7, 9]
        bubble_sort(unsorted_arr)
        self.assertEqual(unsorted_arr, sorted_arr)
    
    def test_merge_sort(self):
        unsorted_arr = [6, 9, 7, 2, 3, 6, 5]
        sorted_arr = [2, 3, 5, 6, 6, 7, 9]
        unsorted_arr = merge_sort(unsorted_arr)
        self.assertEqual(unsorted_arr, sorted_arr)

    def test_quick_sort(self):
        unsorted_arr = [6, 9, 7, 2, 3, 6, 5]
        sorted_arr = [2, 3, 5, 6, 6, 7, 9]
        quick_sort(unsorted_arr, 0, len(unsorted_arr) - 1)
        self.assertEqual(unsorted_arr, sorted_arr)

if __name__ == '__main__':
    unittest.main()