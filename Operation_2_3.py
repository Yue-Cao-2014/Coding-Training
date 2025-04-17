class Solution:
    @staticmethod
    def find_power(x: int) -> list[int]:
        rslt = [0, 0, x]
        if x == 0:
            return rslt

        while x % 2 == 0:
            x = x / 2
            rslt[0] += 1

        while x % 3 == 0:
            x = x / 3
            rslt[1] += 1

        rslt[2] = x

        return rslt

    @staticmethod
    def find_operation_num(x: list[int]) -> int:
        trial = Solution.find_power(x[0])
        max_2 = trial[0]
        max_3 = trial[1]
        left_factor = trial[2]
        record = [[trial[0], trial[1]]]
        ans = 0

        for num in x[1:]:
            tmp = Solution.find_power(num)

            if left_factor != tmp[2]:
                return -1
            
            record.append(tmp[0:2])
            max_2 = max(max_2, tmp[0])
            max_3 = max(max_3, tmp[1])
        
        for tmp in record:
            ans += max_2 - tmp[0]
            ans += max_3 - tmp[1]
        
        return ans
    
if __name__ == "__main__":
    print(Solution.find_operation_num([50, 75, 100]))
    print(Solution.find_operation_num([10, 14]))
    print(Solution.find_operation_num([10, 30, 360]))

