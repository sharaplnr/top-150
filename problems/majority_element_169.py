"""
Дан целочисленный массив размером n, вернуть мажорный элемент.

Мажорный элемент - это элемент, который появляется более [n/2] раз. Можно предположить, что основной элемент
всегда присутствует в массиве.

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

class Solution:
    def majority_element(self, nums: list) -> int:
        len_nums = len(nums)
        condition = len_nums // 2

        s = set(nums)

        for num in s:
            count_num = nums.count(num)

            if count_num > condition:
                return num

        return -1




s = Solution()
print(s.majority_element([3,2,3]))
