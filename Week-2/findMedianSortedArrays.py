"""
4. There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""


class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        length_total = len(nums1) + len(nums2)
        if length_total % 2 == 0:
            return (
                        find_K(length_total // 2, nums1, nums2) +
                        find_K((length_total // 2) - 1, nums1, nums2)
                   ) / 2
        return find_K(length_total // 2, nums1, nums2)


    def find_K(k, nums1, nums2):
        if len(nums1) == 0:
            return nums2[k]
        if len(nums2) == 0:
            return nums1[k]

        mid1 = len(nums1) // 2
        mid2 = len(nums2) // 2

        if k > len(nums1) // 2:
            if nums1[mid1] > nums2[mid2]:
                return find_K(k - mid2 - 1, nums1, nums2[mid2 + 1:])
            else:
                if nums1[mid1] > nums2[mid2]:
                    return find_K(k - mid1 - 1, nums1[mid1 + 1:], nums2)
        else:
            if nums1[mid1] > nums2[mid2]:
                return find_K(k, nums1[:mid1], nums2)
            else:
                return find_K(k, nums1, nums2[:mid2])


def main():
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))


if __name__ == "__main__":
    main()
