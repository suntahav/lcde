class Solution:
    def numDecodings(self, s: str) -> int:
        memoize = {}
        def decode(idx):
            l = len(s[idx:])
            if l == 1 :
                if s[idx] == '0':
                    memoize[idx] = 0
                    return 0
                else:
                    memoize[idx] = 1
                    return 1
            if l == 2:
                if s[idx] == '0':
                    memoize[idx] = 0
                    return 0
                if s[idx + 1] == '0' :
                    if int(s[idx : idx + 2]) <= 26:
                        memoize[idx] = 1
                    else:
                        memoize[idx] = 0
                    return memoize[idx]
                else:
                    if int(s[idx : idx + 2]) <= 26:
                        memoize[idx] = 2
                        return 2
                    else:
                        memoize[idx] = 1
                        return 1
            
            if s[idx] == '0':
                memoize[idx] = 0
                return 0
            elif s[idx + 1] == '0' and int(s[idx:idx+2]) <= 26:
                if idx+2 in memoize:
                    memoize[idx] = memoize[idx+2]
                else:
                    memoize[idx] = decode(idx + 2)

                return memoize[idx]
            else:
                if idx + 1 in memoize:
                    memoize[idx] = memoize[idx+1]
                else:
                    memoize[idx] = decode(idx + 1)

                if int(s[idx : idx + 2]) <= 26:
                    if idx+2 in memoize:
                        memoize[idx] += memoize[idx+2]
                    else:
                        memoize[idx] += decode(idx + 2)
                    
                return memoize[idx]
        result = decode(0)
        
        return result
        