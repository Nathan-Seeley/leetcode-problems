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
    

    import ListNode
        # class ListNode(object):
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
    def mergeTwoLists(self, l1 : ListNode, l2 : ListNode):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        create dummy node to avoid any edge cases
        set tail of list equal to dummy
        Iterate through both lists with condition both are non-empty
        Starting at the beginning of both lists compare the value from list one to list 2
        insert the lesser of the two values into the output
        then move to the next value
        insert remaininder list into new list
        """
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next

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

result = my_solution.mergeTwoLists([1,2,4],[1,3,4])
print (result)