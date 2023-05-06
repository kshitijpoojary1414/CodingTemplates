# Based on right neighbor
class BinarySearchT2 :
    def BinarySearch(nums, target):
        if len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        # Post-processing:
        # End Condition: left == right
        if nums[start] == target:
            return start
        return -1