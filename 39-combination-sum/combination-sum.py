class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        #Could have a case where candidates are duplicate
        candidates = list(set(candidates))

        def calculate(target, current, idx):
            
            #When the target is achieved  base case    
            if target == 0:
                result.append(current)
                return

            #target is less than min but greater
            if target < min(candidates):
                return
            #check all the possible scenarios and idx is the location from where we can start to check further
            for i in range(idx, len(candidates)):
                calculate(target - candidates[i], current + [candidates[i]], i)
        
        calculate(target, [], 0)
        return result

            
            

        