class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_size = 0

        while left < right:
            size = min(height[left], height[right]) * (right - left)

            if size > max_size:
                max_size = size
            
            if height[left] < height[right]:
                left += 1
            else : 
                right -= 1

        return max_size
