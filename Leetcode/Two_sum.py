# coding: utf-8
__author__ = 'lau.wenbo'

"""
Given an array of integers, return indices of 
the two numbers such that they add up to a specific target.
You may assume that each input would have exactly 
one solution, and you may not use the same element twice.
"""


class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

a = Solution()
print a.twoSum(nums=[1,3,2,4],target=5)
