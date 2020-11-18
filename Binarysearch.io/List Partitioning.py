'''
List Partitioning

Given a list of strings strs, containing the strings "red", "green" and "blue", 
partition the list so that the red come before green, which come before blue.
'''


def solve(self, strs):

    colors = {'red': 0, 'green': 0, 'blue': 0}

    for s in strs:
        if s in colors.keys():
            colors[s] += 1

    return(['red']*colors['red']+['green']*colors['green']+['blue']*colors['blue'])
