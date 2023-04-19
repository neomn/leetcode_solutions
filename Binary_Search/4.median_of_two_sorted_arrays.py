
def findMedianSortedArrays(nums1: list[int], nums2:list[int])-> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A


findMedianSortedArrays([1,2,3,4,5], [1,1,2])
