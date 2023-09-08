class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #input: fruits integer list
        #output: maximum number of fruits
        #time complexity O(n)
        #space complexity O(1)
        left = 0
        right = 0
        max_fruits = 0
        fruit_basket = {}
        while right < len(fruits):
            if len(fruit_basket) < 3:
                max_fruits = max(max_fruits, sum(fruit_basket.values()))
                fruit_basket[fruits[right]] = fruit_basket.get(fruits[right], 0) + 1
                right += 1
            else:
                fruit_basket[fruits[left]] -= 1
                if fruit_basket[fruits[left]] == 0:
                    del fruit_basket[fruits[left]]
                left += 1
        if len(fruit_basket) < 3:
            max_fruits = max(max_fruits, sum(fruit_basket.values()))
        return max_fruits