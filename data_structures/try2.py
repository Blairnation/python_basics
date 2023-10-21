# class LongestSubArray:
#     def solve(self, array:[list], k:int) -> int:
#         left = curr = ans = 0

#         for right in range(len(array)):
#             curr += array[right]
#             while curr > k:
#                 curr -= array[left]
#                 left += 1
#             ans = max(ans, right - left + 1)
#         return ans        
    
# arr = [3,1,2,7,4,2,1,1,5]
# k = 8
# array = LongestSubArray()
# ans = array.solve(arr, k)
# print(ans)

class LenOfLongestOnes:
    def solve(self, s):
        left = curr = ans = 0

        for right in range(len(s)):
            if s[right] == '0':
                curr += 1
            while curr > 1:
                if s[left] == '0':
                  curr -= 1
                left += 1
            ans = max(ans, right - left + 1) 

        return ans


s = "1101100111"
lenght = LenOfLongestOnes()
ans = lenght.solve(s)
print(ans)
