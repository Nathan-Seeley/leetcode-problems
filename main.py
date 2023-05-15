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
    
    def romanToInt(self, s):
        """ Changing a Roman Numeral to a Number- 
            Create a dictionary repesenting the roman numeral/number key:value pair
            iterate through input string 
            largest to smallest: add
            smaller before larger: subtract smaller"""
        
        numeral = {"I" : 1,
                   "V" : 5,
                   "X" : 10,
                   "L" : 50,
                   "C" : 100,
                   "D" : 500,
                   "M" : 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and numeral[s[i]] < numeral[s[i+1]]:
                res -= numeral[s[i]]
            else:
                res += numeral[s[i]]
        return res
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        Initialize the result with an empty string
        Iterate through every index of the first string
        Iterate through every single string to make sure 
        all the strings index is inbounds or have the exact same character at index
        
        if not return open string
        add index character that is common to all strings to open string prefix
        return output prefix
        """
        prefix = ""
        
        for i in range(len(strs[0])):
            for s in strs:
               if i == len(s) or s[i] != strs[0][i]:
                   return prefix
            prefix += strs[0][i]
        return prefix

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        Initialize result setting equal to an open list.
        Create dictionary of key value pairs where key is one bracket and value
            is corresponding bracket type.
        Set dictionary equal to new variable.
        Iterate through string to compare parenthesis
        
        """  
        res = []
        bracket_dictionary = {')' : '(',
                             ']' : '[',
                             '}':'{'}
        
        for p in s:
            if p in bracket_dictionary.values():
                res.append(p)
            elif res and bracket_dictionary[p] == res[-1]:
                res.pop()
            else:
                return False
        return res == []
    
    def removeDuplicates(self, nums):
        last = 0
        current = 1

        while last <= current and current < len(nums):
            if nums[last] != nums[current]:
                nums[last + 1] = nums[current]
                last += 1
            current += 1
        return last + 1

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        for number in nums:
            if number != val:
                nums[counter] = number
                counter += 1
        return counter

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
            Define a function named 'strStr' that takes two input strings 'haystack' 
        and 'needle' and returns an integer.
            Calculate the length of the 'haystack' and 'needle' strings 
        and store them in the 'h' and 'n' variables, respectively.
            Extract the first character of the 'needle' string 
        and store it in the 'first_element_of_needle' variable.
            Loop through each index 'i' in the range 0 to 'h-n+1'
                a. Check if the 'i'th character of 'haystack' is equal to the first character of 'needle' 
            and if the next 'n' characters of 'haystack' are equal to 'needle'.
                b. If both the conditions are satisfied, return the current index 'i'.
            If no matching substring is found, return -1.
        """
        h = len(haystack)
        n=len(needle)
        first_needle_element = needle[0]
        for i in range(h-n+1):
            if haystack[i]==first_needle_element and haystack[i:i+n]==needle:
                return i
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        SOLVE-Time complexity:0(logN)
             -Space complexity:0(1)
        Initialize the start pointer equal to 0 and end pointer to lenth of list of integers minus one
        Create conditional loop that runs only when start pointer is less than or equal to end pointer
        Initialize middle pointer equal to the start plus end pointers divide by two discarding remainder
        set conditional that:
            if the number in the middle index position is equal to given target number
                return the matching number.
            if number in middle index position is greater then given target number reduce value of
                end pointer by one
            otherwise start pointer value is increased by one
        return end pointer where it is less then start pointer

        """
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return end + 1
my_solution = Solution()

# result = my_solution.twoSum([2,7,11,15],9)
# print(result)

# result = my_solution.isPalindrome(56765)
# print (result)

# result = my_solution.romanToInt("III")
# print (result)

# result = my_solution.longestCommonPrefix(["flower", "flow", "flight"])
# result = my_solution.longestCommonPrefix(["dog", "racecar","car"])
# print (result)

# result = my_solution.isValid("()")
# print (result)

# result = my_solution.removeDuplicates([1,1,2])
# print (result)

# result = my_solution.removeElement([0,1,4,0,3], 2)
# print (result)

# result = my_solution.strStr("sadbutsad","sad")
# print (result)

result = my_solution.searchInsert([1,3,5,6],5)
print(result)