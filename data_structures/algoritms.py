def check_palindrome(text):
    left = 0
    right = len(text)-1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True


check = check_palindrome('racecar')
print(check)


# ===================================================================================

def sum_to_target(target, items):
    i = 0
    j = len(items)-1
    
    while i < j:
        total = items[i] + items[j]
        if total == target:
            return True
        if total > target:
            j -= 1
        else:
            i  += 1
       
    return False 

target = 13
items = [1,2,3,4,7,8,9,15,17]  
find = sum_to_target(target, items)
print(find)


#==================================================================================

class Solution:
    def isSubsequence(self, str1, str2):
        i = j = 0

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i += 1
            j += 1

        return i == len(str1)        
s1 = 'abc'
s2 = 'sanmdjdkbfck'
solution= Solution()
check = solution.isSubsequence(s1,s2)
print(check)


#======================================================================================

def summer(arr):
    start = 1
    while start < len(arr):
        arr[start] = arr[start] + arr[start - 1]  # Update the current element with the sum of current and previous element
        start += 1
    return arr

arr = [3, 1, 2, 10, 1]
# ans = [3, 4, 6, 16, 17]
ans = summer(arr)
print(ans)
