import pytest
from problems.remove_duplicates_from_sorted_array_26 import Solution

@pytest.mark.parametrize("nums, expected", [([1,1,2], 2), ([0,1,1,1,2,2,3,3,4], 5)])

def test_remove_duplicates_from_sorted_array(nums, expected):
    s = Solution()

    got = s.remove_duplicates(nums)
    want = expected

    assert got == want