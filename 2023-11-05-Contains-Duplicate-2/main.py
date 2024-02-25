'''
https://leetcode.com/problems/contains-duplicate-ii/
Given an integer array nums and an integer k, return true if there are two distinct indices
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

from typing import List

#too slow
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         if(k > len(nums)-1):
#             k=len(nums)-1
#         for i in range(0, len(nums) - 1):
#             print("i:",i," nums[i]:", nums[i])
#             for j in range (i+1, i+k+1):
#                 print("j:",j)
#                 if(j >= len(nums)):
#                     continue
#                 if(nums[i]==nums[j]):
#                     return True
#         return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        valueHash = {}
        for i in range(0, nums.__len__()):
            if(nums[i] in valueHash):
                valueHash[nums[i]].append(i)
            else:
                valueHash[nums[i]] = [i]
        for key in valueHash.keys():
            print ("key: ", key)
            print ("  value: ", valueHash[key])

            if valueHash[key].__len__() > 1:
                curr = 0
                next = 1
                while(next < valueHash[key].__len__()):
                    if abs((valueHash[key][next]-valueHash[key][curr]) <= k):
                        return True
                    else:
                        curr = next
                        next+=1
        return False


#Faster
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         d = {}
#
#         for i, n in enumerate(nums):
#             if n in d and abs(i - d[n]) <= k:
#                 return True
#             else:
#                 d[n] = i
#       return False

if __name__ == '__main__':
    solution = Solution()
    #print(solution.containsNearbyDuplicate([1,2,3,1], 3))
    print(solution.containsNearbyDuplicate([1,0,1,1], 1))
    #print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))
    #print(solution.containsNearbyDuplicate([99,99], 2))
    #print(solution.containsNearbyDuplicate([1,2,3,4,5,6,7,8,9,9], 3))

