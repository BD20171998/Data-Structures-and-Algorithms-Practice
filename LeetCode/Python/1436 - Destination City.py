'''
1436. Destination City
https://leetcode.com/problems/destination-city/submissions/
'''


def destCity(self, paths: List[List[str]]) -> str:

    non_dest = set()

    for i in range(len(paths)):

        if paths[i][0] not in non_dest:
            non_dest.add(paths[i][0])

    for i in range(len(paths)):

        if paths[i][0] not in non_dest:
            return paths[i][0]

        elif paths[i][1] not in non_dest:
            return paths[i][1]
