'''
1604. Alert Using Same Key-Card Three or More Times in a One Hour Period
https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/
'''


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        merged = {k: [] for k in keyName}
        names = []

        for i in range(len(keyName)):

            time = keyTime[i].split(":")
            minutes = int(time[0])*60 + int(time[1])

            merged[keyName[i]].append(minutes)

        for k in merged.keys():
            merged[k].sort()

        for k in merged.keys():

            count = 0
            for i in range(2, len(merged[k])):

                if merged[k][i]-merged[k][i-2] <= 60:

                    names.append(k)
                    break

        return list(sorted(names))
