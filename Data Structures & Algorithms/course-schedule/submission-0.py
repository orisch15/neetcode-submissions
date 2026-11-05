class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        color = {i: "w" for i in range(numCourses)}
        res = False
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(i):
            color[i] = "g"

            for pre in preMap[i]:
                #cycle detected because its in the path
                if color[pre] == "g":
                    return False
                elif color[pre] == "w":
                    #if the previos call detected a cycle we will pump it
                    if not dfs(pre):
                        return False
            color[i] = "b"
            return True

        for i in range(numCourses):
            if color[i] == "w":
                if not dfs(i):
                    return False               
        return True
