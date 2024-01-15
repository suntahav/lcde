from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = Counter([x for _,x in matches])
        winners = set([x for x, _ in matches])

        exact_1 = []
        for key in losers.keys():
            if key in winners:
                winners.remove(key)
            if losers[key] == 1:
                exact_1.append(key)
        
        return [sorted(list(winners)), sorted(exact_1)]