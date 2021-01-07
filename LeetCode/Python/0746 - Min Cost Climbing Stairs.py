'''
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/
'''


def minCostClimbingStairs(self, cost: List[int]) -> int:

    if len(cost) == 2:
        return min(cost[0], cost[1])

    dp = [cost[0], cost[1]]

    for i in range(2, len(cost)):

        dp.append(min(dp[i-2], dp[i-1])+cost[i])

    return min(dp[-1], dp[-2])
