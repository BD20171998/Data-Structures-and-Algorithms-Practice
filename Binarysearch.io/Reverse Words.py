'''
Reverse Words

Given a string of words delimited by spaces, reverse the order of words. For example, given "hello there my friend", 
return "friend my there hello".
'''


def solve(self, sentence):
        
    spl = sentence.split(" ")
    
    rev = [spl[i] for i in range(len(spl)-1,-1,-1)] 
    
    return " ".join(i for i in rev)