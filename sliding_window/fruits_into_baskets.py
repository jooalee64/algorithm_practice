class Solution:
    def totalFruit(fruits) -> int:
        max_len = 0
        left = 0
        basket = {}
        # return the maximum number of fruits you can pick 
        for r in range(len(fruits)):
            basket[fruits[r]] = basket.get(fruits[r], 0) + 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            max_len = max(max_len, r-left+1)
        return max_len
                
    # write in a class
    # fruits = [1,2,3,2,2] #4
    # fruits = [1,2,1] #3
    fruits = [0,1,2,2] #3
    result = totalFruit(fruits)
    print(result)
    # def totalFruit(self, fruits: List[int]) -> int:

        