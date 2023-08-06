class Solution:
    def checkEqualHash(self, h1, h2):
        flag = True
        for k in h2.keys():
            if k in h1:
                if h1[k] < h2[k]:
                    flag = False
            else:
                flag = False
        return flag
    def minWindow(self, s: str, t: str) -> str:
        lp, rp = 0, 0
        hash_map = {}
        for c in t:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1
        res = ""
        temp_map = {}
        while rp < len(s):
            # print(rp)
            # print("-----",lp)
            flag = True
            # Add to temp map when moving rp if present in original hashmap
            if s[rp] in hash_map:
                if s[rp] in temp_map:
                    temp_map[s[rp]] += 1
                else:
                    temp_map[s[rp]] = 1
                
            #Check if all chars in current substring
            if self.checkEqualHash(temp_map, hash_map):
                
                #Shortening the string
                while lp < len(s):
                    if s[lp] not in temp_map:
                        lp += 1
                    elif temp_map[s[lp]] > hash_map[s[lp]]:
                        temp_map[s[lp]] -= 1
                        lp += 1
                        
                    else:
                        break
                if res == "":
                    res = s[lp:rp+1]
                else:
                    if len(s[lp:rp+1]) < len(res):
                        res = s[lp:rp+1]
                if s[lp] in temp_map:
                    temp_map[s[lp]] -= 1
                lp += 1
                # flag = False
                # print(res)
                
                if lp >= len(s):
                    break
                

            #Increment right pointer
            if flag:
                rp += 1
        
        #final shrink
        while lp < len(s) and (s[lp] not in temp_map):
            lp += 1
        
        if self.checkEqualHash(temp_map, hash_map):
            if res == "":
                res = s[lp:rp+1]
            else:
                if len(s[lp:rp+1]) < len(res):
                    res = s[lp:rp+1]
        
        return res
            
