class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(candidates)
        def helper(cur ,cur_sum,idx):
            if cur_sum>target:# boundary condition
                return
            # if i==len(candidates):
            if cur_sum==target:# base condition
                ans.append(cur)
                # print(ans)
                return            
            for i in range(idx, n):
 		helper(cur + [candidates[i]], cur_sum + candidates[i], i)

        helper([],0,0)
        return ans