'''
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

'''


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = {}
    final_list = []

    for i in strs:
        temp = [j for j in i]
        temp.sort()
        temp2 = "".join(temp)

        if temp2 not in anagrams:
            anagrams[temp2] = [i]

        else:
            anagrams[temp2].append(i)

    for key, value in anagrams.items():
        final_list.append(anagrams[key])

    return final_list
