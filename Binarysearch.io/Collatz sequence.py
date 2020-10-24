'''
Collatz sequence

Given a positve integer n, find the length of its Collatz sequence. 
Collatz sequence is generated sequentially where
	•	n = n / 2 if n is even
	•	n = 3 * n + 1 if n is odd
	•	And the sequence ends if n = 1
'''


def solve(self, n):

    seq = [n]

    i = 1

    while n != 1:

        if n % 2 == 0:
            n //= 2
            seq.append(n//2)

        else:
            n = 3*n+1
            seq.append(3*n+1)

    return len(seq)
