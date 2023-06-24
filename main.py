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
    
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :type: int
        
        """
        return (len(s.split()[-1])) 
    
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        reverse digits array
        create variables: 
            one representing the carry over number 
            another representing the index of the digit we are currently at
        create while loop to iterate through the given digits
            with condition that the carry number is equal to 1
        within loop check that the digit location is within or out of bounds
            if within:
                create a special case where if the digit is 9 then that digit is reset to zero
                otherwise increment the digit by one and set the carry to zero
            if out of bounds:
                add a new digit to array
                reset carry to 0 thus terminating the while loop
            increment index of while loop  
        reverse new digits array
        """
        digits = digits[::-1]
        carry = 1
        index = 0

        while carry:
            if index < len(digits):
                if digits[index] == 9:
                    digits[index] = 0
                else:
                    digits[index] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            index += 1
        return digits[::-1]
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        create result variable equal to open string
        initialize pointer i and j to end of a and b 
        initialize carry equal to zero
        add carry to the sum of a[i] and b[j] if applicable
        move pointers to the next digit
        update carry based on sum
        append the binary digit to result string
        append carry to result string if it exists
        return reversed result string
        """
        res = ""
        i = len(a) - 1
        j = len(b) - 1

        carry = 0

        while i >= 0 or j >= 0:
            sum = carry

            if i>=0:
                sum += ord(a[i]) - ord('0')
            if j >= 0:
                sum += ord(b[j]) - ord('0')

            i = i - 1
            j = j - 1

            carry = 1 if sum > 1 else 0
            res += str(sum % 2)

        if carry != 0:
            res += str(carry)

        return res[::-1]
    
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        
        """
        res = x
        while not res * res - x < 1:
            res = (res + x / res) / 2
        return int(res)
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        account for first two steps
        set counter -num_of_ways- equal to zero
        """
        if n <= 2:
            return n
        
        num_of_ways = 0

        two_below_current_step = 1 # 2 steps below 3 -ways to take 1 step: 1
        one_below_current_step = 2 # 1 step below 3 - ways to take 2 steps: 2

        for i in range(3, n+1):
            # compute number of ways for i
            num_of_ways = one_below_current_step + two_below_current_step
            # step up to i + 1
            # 1 step below becomes 2 steps below
            # current number of ways becomes 1 step below
            two_below_current_step = one_below_current_step
            one_below_current_step = num_of_ways
        return num_of_ways

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if nums1[m-1] >= nums2[n-1] and m>0:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1]= nums2[n-1]
                n -= 1
        return nums1
    
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        for i in range(numRows):
            if(i == 0):
                # Create a list to store the prev triangle value for further addition...
                # Inserting for the first row & store the prev array to the output array...
                prev = [1]
                output.append(prev)
            else:
                curr = [1]
                j = 1
                # Calculate for each of the next values...
                while(j < i):
                    # Inserting the addition of the prev arry two values...
                    curr.append(prev[j-1] + prev[j])
                    j+=1
                # Store the number 1...
                curr.append(1)
                # Store the value in the Output array...
                output.append(curr)
                # Set prev is equal to curr...
                prev = curr
        return output 

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        res=[]
        for i in range(rowIndex+1):
            res.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j - 1] + res[i - 1][j])
        return res[rowIndex] 
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            currentProfit = prices[sell]-prices[buy]
            if prices[buy] < prices[sell]:
                max_profit = max(currentProfit,max_profit)
            else:
                buy = sell
            sell += 1
        return max_profit
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Compare against reverse
        # Adjust string so that it is free of spaces or comma's
        # Create a reverse string
        # Compare reverse string and s if they match then string is a palindrome

        import re

        s = re.sub(r'[^09a-zA-Z]', '',s).lower()
        
        rev_string = s[::-1]

        return rev_string == s
    
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0

        for num in nums:
            counter ^= num
        return counter

    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = ""
        while columnNumber:
            res += chr(ord("A") + (columnNumber - 1) % 26)
            columnNumber = (columnNumber -1) // 26

        return res[::-1]
    
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Create two variables: one to keep track of the current majority element and the other
            to store the count of the majority
        Iterate through integers of numbers whereby if the integer is equal to the current majority
            then one is added to the count. If it is not the same then subtract one from the count.
        Account for the count of the current majority to be zero by changing the majority element
            and start its count from 1
        return current majority element
        """
        
        current = None
        counter = 0

        for i in nums:
            if counter == 0:
                current = i
            counter += (1 if i == current else -1)
        return current
        
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        string = 0
        for ch in columnTitle:
            string = string * 26 + ord(ch) - ord('A') + 1
        return string
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

# result = my_solution.searchInsert([1,3,5,6],5)
# print(result)

# result = my_solution.lengthOfLastWord("    fly me    to    the moon    ")
# print(result)

# result = my_solution.plusOne([4,3,2,1])
# print(result)

# result = my_solution.addBinary("11", "1")
# print (result)

# result = my_solution.mySqrt(4)
# print (result)

# result = my_solution.climbStairs(45)
# print (result)

# result = my_solution.merge([1,2,3,0,0,0],3,[2,5,6],3)
# print (result)

# result = my_solution.generate(5)
# print (result)

# result = my_solution.getRow(3)
# print (result)

# result = my_solution.maxProfit([7,1,5,3,6,4])
# print (result)

# result = my_solution.isPalindrome("A man, a plan, a canal: Panama")
# print(result)

# result = my_solution.singleNumber([2,2,1])
# print (result)

# result = my_solution.convertToTitle(28)
# print(result)

# result = my_solution.majorityElement([1,1,1,1,2,2,2,3,3,3])
# result = my_solution.majorityElement([6,5,5,])
# print(result)

result = my_solution.titleToNumber("ZY")
print (result)