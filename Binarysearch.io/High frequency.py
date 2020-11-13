'''
High frequency

Given a list of integers nums, find the most frequently occurring element and return the 
number of occurrences of that element.
For example, given the list [1, 4, 1, 7, 1, 7, 1, 1], return 5 since the the element 1 appears 5 times.
'''

def solve(self, nums):
        
    num_sets={k:0 for k in set(nums)}
    num_max =0
    for k in nums:
        
        num_sets[k]+=1
    
    for k in num_sets.keys():
        
        if num_sets[k] > num_max:
            num_max = num_sets[k]
            
    return num_max