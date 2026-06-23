class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, target, path):
            if target == 0:
                res.append(path.copy())
                return
            for i in range(start, len(candidates)):
                val = candidates[i]
                if val > target:
                    break
                path.append(val)
                dfs(i, target - val, path)
                path.pop()

        dfs(0, target, [])
        return res
        