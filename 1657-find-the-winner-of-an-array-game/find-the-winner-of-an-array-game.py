class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = max(arr[0], arr[1])
        counter = 1
        for i in range(2, len(arr)):
            if counter == k:
                return winner
            if winner == max(winner, arr[i]):
                counter += 1
            else:
                winner = max(winner, arr[i])
                counter = 1
        return winner
        