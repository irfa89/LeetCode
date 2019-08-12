"""
210. There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the
ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.

"""

import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):

        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        path = []
        for i in range(numCourses):
            zeroDegree = False
            for j in range(numCourses):
                if indegrees[j] == 0:
                    zeroDegree = True
                    break
            if not zeroDegree:
                return []
            indegrees[j] -= 1
            path.append(j)
            for node in graph[j]:
                indegrees[node] -= 1
        return path


def main():
    sol = Solution()
    print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))


if __name__ == "__main__":
    main()

