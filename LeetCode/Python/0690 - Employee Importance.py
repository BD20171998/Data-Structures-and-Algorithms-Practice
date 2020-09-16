'''
690. Employee Importance
https://leetcode.com/problems/employee-importance/
'''

# Definition for Employee.
# class Employee:
#     def __init__(self, id: int, importance: int, subordinates: List[int]):
#         self.id = id
#         self.importance = importance
#         self.subordinates = subordinates


def getImportance(self, employees: List['Employee'], id: int) -> int:

    emps = {}

    for employee in employees:
        emps[employee.id] = employee

    def dfs(id):

        total_imp = emps[id].importance

        for ee in emps[id].subordinates:
            total_imp += dfs(ee)

        return total_imp

    return dfs(id)
