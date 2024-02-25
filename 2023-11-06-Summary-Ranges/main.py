'''
https://leetcode.com/problems/summary-ranges/
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums
 is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
'''

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums.__len__() == 0:
            return []
        if nums.__len__() == 1:
            return [f"{nums[0]}"]
        currentRange = ''
        ranges = []
        beginning = nums[0]
        prev = nums[0]
        end = None;
        for i in range(1,len(nums)):
            curr = nums[i]
            print("Curr:",curr)
            print ("Prev:", prev)
            if curr - prev > 1:
                end = prev
                print("hi")
                if end != beginning:
                    print("Hi")
                    currentRange = f"{beginning}->{end}"
                else:
                    print("HI")
                    currentRange = f"{end}"
                ranges.append(currentRange)
                beginning = curr
                prev = curr
            else:
                prev = curr
            if i == len(nums)-1:
                end = prev
                if end != beginning:
                    print("Hi2")
                    currentRange = f"{beginning}->{end}"
                else:
                    print("HI2")
                    currentRange = f"{end}"
                ranges.append(currentRange)
        return ranges

if __name__ == '__main__':
    solution = Solution()
    print(solution.summaryRanges([0,1,2,4,5,7]))

