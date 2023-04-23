class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]


        """

        for index_a, value_a in enumerate(nums):
            for index_b, value_b in enumerate(nums):
                if value_a + value_b == target and index_a != index_b:
                    return [index_a, index_b]

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

        """

        if x <0:
            return False
        
        num = x
        new_num = 0
        while x > 0:
          
            new_num = new_num * 10 + x % 10
            x //= 10
        return new_num == num
    

        
my_solution = Solution()

# result = my_solution.twoSum([2,7,11,15],9)
# print(result)

result = my_solution.isPalindrome(56765)
print (result)
