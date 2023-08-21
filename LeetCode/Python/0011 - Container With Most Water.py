'''
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:


        l, r = 0, len(height)-1

        area = 0
        h = 0

        while l < r:
            h = min(height[l],height[r])
            temp_area = (r -l) * h

            if temp_area >= area:

                area = temp_area

            if height[l] >= height[r]:
                r = r -1

            else:
                l = l+1

        return area