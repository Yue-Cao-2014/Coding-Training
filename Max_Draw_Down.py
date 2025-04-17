import pandas as pd

class Solution:

    @staticmethod
    def find_max_draw_down(price: pd.Series) -> tuple[float, int, int]:

        if len(price) < 2:
            return (0.0, None, None)

        peak = price[0]
        max_dd = 0
        peak_index = 0
        start_index = 0
        end_index = 0

        for i, p in enumerate(price):
            if peak < p:
                peak = p
                peak_index = i
            else:
                dd = (price[peak_index] - p)
                if max_dd < dd:
                    max_dd = dd
                    start_index = peak_index
                    end_index = i

        return max_dd, start_index, end_index
    
    @staticmethod
    def find_two_max_draw_down(price: pd.Series) -> tuple[float, int, int, float, int, int]:
        max_dd, start_index, end_index = Solution.find_max_draw_down(price)

        if max_dd <= 0:
            return max_dd, start_index, end_index, 0, None, None
        
        tmp = price[price.index < start_index]
        left_dd, l_start_index, l_end_index = Solution.find_max_draw_down(tmp)

        tmp = price[price.index > end_index]
        right_dd, r_start_index, r_end_index = Solution.find_max_draw_down(tmp)

        if left_dd > right_dd:
            return max_dd, start_index, end_index, left_dd, l_start_index, l_end_index
        else:
            return max_dd, start_index, end_index, right_dd, r_start_index, r_end_index


if __name__ == "__main__":
    s = pd.Series([1,3,2,5,4,3,2])
    print(Solution.find_two_max_draw_down(s))
    s = pd.Series([100, 90, 80, 70, 60])
    print(Solution.find_two_max_draw_down(s))
    s = pd.Series([1, 2, 3, 4, 5])
    print(Solution.find_two_max_draw_down(s))