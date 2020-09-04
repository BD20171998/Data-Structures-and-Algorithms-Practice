'''
1328. Break a Palindrome
https://leetcode.com/problems/break-a-palindrome/
'''

    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome) == 1:
            return ""
        
        broken = [i for i in palindrome]
        i = 0
        
        while i < len(palindrome)//2:
            if broken[i] != "a":
                break
            i+=1
            
        if i == len(palindrome)//2:
            broken[len(palindrome)-1] = "b"
            return "".join(broken)
        
        for i in range(len(palindrome)):
            if broken[i] != "a":
                broken[i] = "a"
                break
    
        return "".join(broken)