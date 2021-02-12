'''
Steady Speed

You are given a list of integers positions representing the 
position of a car at equally spaced intervals of time. Return 
the length of the longest sublist where the car was traveling 
at a constant speed.
'''


def solve(self, positions):

    count = 1
    start = 0

    diff = abs(positions[1]-positions[0])

    for i in range(1, len(positions)):

        if abs(positions[i]-positions[i-1]) == diff:
            count = max(i-start+1, count)

        else:
            diff = abs(positions[i]-positions[i-1])
            start = i-1

    return count
