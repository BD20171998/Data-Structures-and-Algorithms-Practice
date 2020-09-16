'''
1041. Robot Bounded In Circle
https://leetcode.com/problems/robot-bounded-in-circle/
'''


def isRobotBounded(self, instructions: str) -> bool:

    north = (0, 1)
    west = (-1, 0)
    south = (0, -1)
    east = (1, 0)
    rotations = {north: {"R": east, "L": west},
                 west: {"R": north, "L": south},
                 south: {"R": west, "L": east},
                 east: {"R": south, "L": north}}

    seen = {}
    position = (0, 0)
    facing = north
    seen[position] = facing

    for _ in range(4):
        for instruction in instructions:

            if instruction is "G":
                position = (position[0] + facing[0],
                            position[1] + facing[1])

            else:
                facing = rotations[facing][instruction]

        if position in seen:
            return True

    if position in seen:
        return True

    return False
