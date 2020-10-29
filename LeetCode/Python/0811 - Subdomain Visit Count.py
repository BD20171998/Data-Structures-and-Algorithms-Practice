'''
811. Subdomain Visit Count
https://leetcode.com/problems/subdomain-visit-count/
'''


def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

    mydict = {}

    def add(count, string):

        for i in range(len(string)-1, -1, -1):

            temp = ".".join(string[i:len(string)])

            if temp not in mydict:
                mydict[temp] = count

            else:
                mydict[temp] += count

    for i in cpdomains:

        t1 = i.split(" ")
        count = int(t1[0])
        string = t1[1].split(".")
        add(count, string)

    return ["{} {}".format(v, k) for (k, v) in mydict.items()]
