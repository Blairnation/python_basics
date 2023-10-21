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
