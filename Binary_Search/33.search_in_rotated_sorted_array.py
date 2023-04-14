
def search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r) >> 1
        if nums[mid] == target:
            return mid
        
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid+1
            




            

search([4,5,6,7,0,1,2], 0)
