class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def calculate(idx, s):
            if idx == len(arr):
                return len(s)
            
            if len(set(s).intersection(set(arr[idx]))) == 0 and len(s) == len(set(s)) and len(arr[idx]) == len(set(arr[idx])):
                #Means unique element in new string and current string

                #Include current index string
                inc = calculate(idx+1, s+arr[idx])
                ninc = calculate(idx+1, s)
                return max(inc, ninc)
            return calculate(idx+1, s)
        
        return calculate(0, "")


        