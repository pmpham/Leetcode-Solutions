# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# O(n+m/2) 
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenBoth = len(nums1) + len(nums2)
        
        # for odd
        if lenBoth%2 ==1:
            midpoint = (lenBoth//2) +1
            p1 = p2 = 0
            curr = 0
            for i in range(midpoint):
                if p1<len(nums1) and p2<len(nums2):
                    if nums1[p1]<nums2[p2]:
                        curr = nums1[p1]
                        p1+=1
                    else:
                        curr = nums2[p2]
                        p2+=1
                else:
                    if p1<len(nums1):
                        curr = nums1[p1]
                        p1+=1
                    else:
                        curr = nums2[p2]
                        p2+=1
        #for even
        else:
            midpoint = lenBoth//2
            p1 = p2 = 0
            curr = 0
            for i in range(midpoint):
                if p1<len(nums1) and p2<len(nums2):
                    if nums1[p1]<nums2[p2]:
                        curr = nums1[p1]
                        p1+=1
                    else:
                        curr = nums2[p2]
                        p2+=1
                else:
                    if p1<len(nums1):
                        curr = nums1[p1]
                        p1+=1
                    else:
                        curr = nums2[p2]
                        p2+=1
            if p1<len(nums1) and p2<len(nums2):
                    if nums1[p1]<nums2[p2]:
                        curr += nums1[p1]
                        p1+=1
                    else:
                        curr += nums2[p2]
                        p2+=1
            else:
                    if p1<len(nums1):
                        curr += nums1[p1]
                        p1+=1
                    else:
                        curr += nums2[p2]
                        p2+=1
            curr = float(curr)/2
        return curr
        
        #for even