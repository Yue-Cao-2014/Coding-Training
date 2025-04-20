class Solution:
    @staticmethod
    def find_min_opration(egg: int, floor: int) -> int:
        """
        Find min operation to find floor number using #egg on a 
        floor#-building.
        """
        # ith means maxium floor to test with i eggs.
        ans = [0] * (egg + 1)
        # m is the trial number
        trial = 0

        while ans[-1] < floor:
            trial += 1
            prev = 0
            for i in range(1, egg + 1):
                tmp = ans[i]
                ans[i] += prev + 1
                prev = tmp

        return trial
    
if __name__ == "__main__":
    print(Solution.find_min_opration(1, 100))
    print(Solution.find_min_opration(2, 100))
    print(Solution.find_min_opration(2, 36))