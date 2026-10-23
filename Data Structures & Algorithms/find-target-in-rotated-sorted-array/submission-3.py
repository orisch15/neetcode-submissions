class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
#שחלוקת שלמים // 2 מעגלת תמיד כלפי מטה. כשיש שני איברים סמוכים, m תמיד יהיה שווה ל-l. לכן השמה של l = m לא משנה דבר.
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # 1. האם החצי השמאלי ממוין?
            if nums[l] <= nums[m]:
                # האם המטרה בתוך התחום הממוין השמאלי?
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # 2. אחרת, החצי הימני בהכרח ממוין
            else:
                # האם המטרה בתוך התחום הממוין הימני?
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


        