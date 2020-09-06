'''
71. Simplify Path
https://leetcode.com/problems/simplify-path/
'''

def simplifyPath(self, path: str) -> str:
        
        if path == "/":
            return "/"
        
        canonical_str = []
        
        split_path = path.split("/")
       
        for i in split_path:
            if i == "" or i ==".":
                continue
                
            elif i == "..":
                if len(canonical_str) < 1:
                    continue
                    
                else:
                    canonical_str.pop()
                    
            else:
                canonical_str.append("/" + i)
          
        if canonical_str == []:
            return "/"
        
        return "".join(canonical_str)