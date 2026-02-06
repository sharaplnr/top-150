import pytest
from problems.merge_sorted_array_88 import Solution

@pytest.mark.parametrize('nums1, m, nums2, n, expected_list', [
    ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1])
])
def test_merge_sorted_array(nums1, m, nums2, n, expected_list):
    s = Solution()

    got = s.merge(nums1=nums1, nums2=nums2, n=n, m=m)
    want = expected_list

    assert got == want