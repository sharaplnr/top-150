"""
Дано два отсортированных массива в порядке возрастания и дано два числа, представляющее кол-во элементов в этих массивах;
Необходимо объединить два массива в порядке возрастания.

Изменения необходимо в рамках массива nums1. Длина окончательного массива m + n
"""

class Solution:

    def merge(self, nums1: list, m: int, nums2: list, n: int):
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n-1]
            last -= 1
            n -= 1

        return nums1