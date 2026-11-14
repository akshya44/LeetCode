class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        answer = float('inf')

        for i in range(n):
            total = 0

            for j in range(i, min(i + r, n)):
                total += nums[j]

                length = j - i + 1

                if l <= length <= r and total > 0:
                    answer = min(answer, total)

        return answer if answer != float('inf') else -1