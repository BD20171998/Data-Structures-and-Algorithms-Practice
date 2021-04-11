'''
Detect Voter Fraud

Given a two dimensional 
list of integers votes, 
where each list has two 
elements [candidate_id, voter_id], 
report whether any voter 
has voted more than once.
'''


class Solution:
    def solve(self, votes):

        voters = []

        voters = [v[1] for v in votes]

        if len(set(voters)) == len(voters):
            return False

        else:
            return True
