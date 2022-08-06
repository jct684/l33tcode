class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #any number to the right that is higher results in no ocean view
        #track highest number compared to current index from right to left to determine ocean view
        #add index to array if the highest number is lower than current number from right to left
        #reverse at the end to match expected output
        #O(n) time complexity where n is length of input heights
        #O(k) space complexity where k is length of output buildings, no ohter space needed
        tallest = heights[-1]
        ocean_view = [len(heights)-1]
        for i in range (len(heights)-2, -1, -1):
            if heights[i]>tallest:
                ocean_view.append(i)
                tallest = heights[i]
        return ocean_view[::-1]
