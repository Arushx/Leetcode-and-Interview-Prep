class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_keys = list(set(nums))
        counts = {key : nums.count(key) for key in unique_keys}

        final = []
        for _ in range(k):
            max_key = max(counts, key=counts.get)
            final.append(max_key)
            counts.pop(max_key)
        
        return final
# NEED TO COME BACK TO THIS

        