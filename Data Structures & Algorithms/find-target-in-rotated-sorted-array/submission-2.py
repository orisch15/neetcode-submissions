class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
#שחלוקת שלמים // 2 מעגלת תמיד כלפי מטה. כשיש שני איברים סמוכים, m תמיד יהיה שווה ל-l. לכן השמה של l = m לא משנה דבר.
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] > nums[r]: #so m is in the left part
                if target > nums[m] :
                    l = m + 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else: #mid is in the right part
                if target < nums[m]:
                    r = m - 1
                elif target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1 
        return -1


        