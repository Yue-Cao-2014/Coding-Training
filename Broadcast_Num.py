class Solution:
    @staticmethod
    def compute_key(x: int) -> int:
        """
        Compute difference between original number and reversed number.
        """
        tmp = str(x)
        tmp = tmp[::-1]
        tmp = int(tmp)

        return x - tmp
    
    @staticmethod
    def find_math(nums: list[int]) -> int:
        """
        Find match among students
        """
        dict_key = {}
        rslt = 0
        for num in nums:
            tmp = Solution.compute_key(num)
            if tmp in dict_key:
                dict_key[tmp] += 1
            else:
                dict_key[tmp] = 1
        
        for key in dict_key:
            match = dict_key[key]
            rslt += match * (match - 1) / 2

        rslt = rslt % (pow(10, 9) + 7)
        return int(rslt)
    
if __name__ == "__main__":
    print(Solution.find_math([17, 28, 39, 71]))
    print(Solution.find_math([71, 60]))