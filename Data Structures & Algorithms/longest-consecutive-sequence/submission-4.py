class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #edge case
        if len(nums)==0:return 0
        snums = set(nums)
        seq = 1
        best = 1
        cont = 0
        for n in nums:
            if n-1 not in snums:
                cont = n + 1
                seq = 1
                while cont in snums:
                    seq += 1
                    cont += 1
                best = max(best, seq)
                
        return best
        