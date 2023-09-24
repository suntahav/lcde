class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        mapper = {}
        sums1 = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sums1.append(nums1[i] + nums2[j])
        sums2 = []
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                sums2.append(nums3[i] + nums4[j])

        for n in sums2:
            if n in mapper:
                mapper[n] += 1
            else:
                mapper[n] = 1
        count = 0
        for n in sums1:
            if -n in mapper:
                count += mapper[-n]
        return count