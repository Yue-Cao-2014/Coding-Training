class Solution:
    @staticmethod
    def find_combination(total_val: int, coins: list[int], 
                         max_note: int) -> int:
        """
        Find max possible combination for total value using
        coin in coins.
        """
        m = max_note + 1
        n = total_val + 1
        coins.sort()
        ans = [[0] * n for _ in range(m)]
        ans[0][0] = 1

        for c in coins:
            for i in range(1, m):
                for j in range(c, n):
                    ans[i][j] += ans[i - 1][j - c]

        return sum(ans[i][-1] for i in range(m))
    

if __name__ == "__main__":
    print(Solution.find_combination(100, [1, 2, 5, 10, 20, 50], 2))