'''
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/
'''


def orangesRotting(self, grid: List[List[int]]) -> int:

    minutes = 0
    fresh = []
    rotten = {}
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for x in range(len(grid)):
        for y in range(len(grid[x])):

            if grid[x][y] == 1:
                fresh.append((x, y))

            elif grid[x][y] == 2:
                rotten[(x, y)] = 2

    while len(fresh) > 0:

        infected = {}

        for key in rotten.keys():

            for i in directions:
                check = (key[0]+i[0], key[1]+i[1])

                if check in fresh:
                    fresh.remove(check)
                    infected[check] = 2

        if len(infected) == 0:
            return -1

        for k, v in infected.items():
            rotten[k] = v

        minutes += 1

    return minutes
