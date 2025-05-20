def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    area = 0

    i = 0
    j = len(height) - 1
    
    while i < j:
        new = min(height[i], height[j]) * (j-i)
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
        area = max(new, area)
    
    return area