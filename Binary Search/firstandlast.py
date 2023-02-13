#This python program is to find the first occurance and the last occurance of a number in an array. 
#For example, in the array below, target = 5 appears first at 6th index and last at 10th index so out output must be [5,10]

nums = [1,1,2,2,3,3,5,5,5,5,5,6]
target = 5

class Solution:
    def searchRange(self,nums,target):
        return [self.findFirstOccurrence(nums, target), self.findLastOccurrence(nums, target)]
              
    def findFirstOccurrence(self,nums, target):
        left, right = 0, len(nums) - 1
        firstOccurrence = -1
        while left <= right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                firstOccurrence = middle
                right = middle - 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return firstOccurrence
    
    def findLastOccurrence(self,nums, target):
        left, right = 0, len(nums) - 1
        lastOccurrence = -1
        while left <= right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                lastOccurrence = middle
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return lastOccurrence

print(Solution().searchRange(nums, target))