import pytest
from problems.majority_element_169 import Solution

@pytest.mark.parametrize("nums, expected", [([3,2,3], 3), ([2,2,1,1,1,2,2], 2)])
def test_majority_element(nums, expected):
    got = Solution().majority_element(nums)
    want = expected

    assert got == want