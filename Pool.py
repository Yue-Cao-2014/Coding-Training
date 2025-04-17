class Solution:
    def __init__(self, pool: list[str]):
        self.c = len(pool[0])
        self.r = len(pool)
        self.dir = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1],
                    [-1, 1], [-1, 0], [-1, -1]]
        self.pool = pool
        self.flag = [[False for i in range(self.c)] for j in range(self.r)]
    
    def check(self, coor_x: int, coor_y: int) -> bool:
        """
        Check if the direction is allowed.
        """
        if coor_x > -1 and coor_x < self.r and coor_y > -1 and coor_y < self.c:
            return True
        
        return False

    def dfs(self, coord_x: int, coord_y: int) -> None:
        """
        Deep first search
        """
        self.flag[coord_x][coord_y] = True

        for dir in self.dir:
            new_x = coord_x + dir[0]
            new_y = coord_y + dir[1]
            check = self.check(new_x, new_y)

            if check and self.pool[new_x][new_y] == "W" and not self.flag[new_x][new_y]:
                self.dfs(new_x, new_y)

    def compute_pool_num(self) -> int:
        """
        Compute number of pools.
        """
        
        ans = 0

        for i in range(self.r):
            for j in range(self.c):
                if not self.flag[i][j] and self.pool[i][j] == "W":
                    self.dfs(i, j)
                    ans += 1

        return ans
    
if __name__ == "__main__":
    test = Solution([".....W", ".W..W.", "....W.", ".W....",
                    "W.WWW.", ".W...."])
    print(test.compute_pool_num())
    test = Solution(["W....W", ".W..W.", "..W.W.", "W..W..",
              "W.W...", ".W...."])
    print(test.compute_pool_num())