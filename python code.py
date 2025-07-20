class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        # Function to find the maximum number formed by k digits from the given list
        def find_max_sequence(nums: List[int], k: int) -> List[int]:
            stack = [0] * k  # Initialize a stack to store the max number sequence
            to_remove = len(nums) - k  # Calculate how many digits we can remove
            top = -1

            for num in nums:
                while top >= 0 and stack[top] < num and to_remove > 0:
                    top -= 1  # Pop from stack
                    to_remove -= 1
                if top + 1 < k:  # If there is space in stack, push the current number
                    top += 1
                    stack[top] = num
                else:
                    to_remove -= 1

            return stack

        # Compare two sequences to determine which one is greater
        def is_greater(nums1: List[int], nums2: List[int], i: int, j: int) -> bool:
            while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                i += 1
                j += 1
            return j == len(nums2) or (i < len(nums1) and nums1[i] > nums2[j])

        # Merge two sequences into the largest possible number
        def merge(nums1: List[int], nums2: List[int]) -> List[int]:
            merged = []
            i = j = 0
            while i < len(nums1) or j < len(nums2):
                if is_greater(nums1, nums2, i, j):
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            return merged
      
        # Iterate through all possible splits of k between nums1 and nums2
        best_sequence = [0] * k
        for count in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            candidate1 = find_max_sequence(nums1, count)
            candidate2 = find_max_sequence(nums2, k - count)
            candidate_merged = merge(candidate1, candidate2)
            if best_sequence < candidate_merged:
                best_sequence = candidate_merged
              
        return best_sequence
