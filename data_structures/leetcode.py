# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# code
class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}  
        
        for i, num in enumerate(nums):
            if num in num_dict:
                return [num_dict[num], i]
            
            complement = target - num
            num_dict[complement] = i
        
        return []  

nums = [3, 2, 4]
target = 6
solution = Solution()
ans = solution.twoSum(nums, target)
print(ans)

# ==================================================================================================================

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        string_set = set()  # To keep track of unique characters in the current window
        max_length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in string_set:
                string_set.remove(s[left])  # Remove characters from the left side of the window
                left += 1
            string_set.add(s[right])  # Add the current character to the window
            max_length = max(max_length, right - left + 1)  # Update the maximum length
        
        return max_length

s = "abcabbcb"
length = Solution()
ans = length.lengthOfLongestSubstring(s)
print(ans)


#========================================================================================================================


def lenOfLongestSubArray(arr, target):
    left = curr = length = 0

    for right in range(len(arr)):
        curr += arr[right]
        while curr > target:
            curr -= arr[left]
            left += 1
        length = max(length, right - left + 1)    
    return length

arr = [3,1,2,7,4,2,1,1,5]
k = 8
lenght = lenOfLongestSubArray(arr, k)
print(lenght)



#====================================================================================================================

def removeDuplicates(nums):
    if not nums:
        return 0
    
    left = 0
    for right in range(1,len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]
    return left + 1   

 

nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
k = removeDuplicates(nums)
print(k)  # Output: 5 (nums = [1, 2, 3, 4, 5, 2, 4, 4, 5])



# ========================================================================================================================

def find_lenght(string):
    left = curr = ans = 0

    for right in range(len(string)):
        if string[right] == '0':
            curr += 1
        while curr > 1:
            if string[left] == '0':
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

string = '110010110'   
ans = find_lenght(string)
print(ans)             


#========================================================

class SortedArray:
    def sort(self,arr):
       sorted_list = []
       
       for num in range(len(arr)):
           small = min(arr)
           sorted_list.append(small)
           arr.remove(small)
       return sorted_list    

                  
arr = [5,70,3,1,24,14,32]
num = SortedArray() 
print(num.sort(arr))    
