class Solution:
    def sortColors(self, nums):
        low, middle, high = 0, 0, len(nums) - 1
        
        while middle <= high:
            if nums[middle] == 0:
                # Swap nums[low] and nums[middle] and move both pointers
                nums[low], nums[middle] = nums[middle], nums[low]
                low += 1
                middle += 1
            elif nums[middle] == 1:
                # Move the middle pointer
                middle += 1
            else:  # nums[middle] == 2
                # Swap nums[middle] and nums[high] and move the high pointer
                nums[high], nums[middle] = nums[middle], nums[high]
                high -= 1

# Example usage
solution = Solution()
nums = [2,0,2,1,1,0]
solution.sortColors(nums)
print(nums)  # Output: [0,0,1,1,2,2]

nums = [2,0,1]
solution.sortColors(nums)
print(nums)  # Output: [0,1,2]
