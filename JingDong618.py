def get_min_amount(prices):
    if not prices:
        return 0
    min_single = min(prices)
    n = len(prices)
    dp = [False] * 200
    dp[0] = True
    min_sum = float('inf')
    
    for p in prices:
        new_dp = dp[:]
        for s in range(200):
            if dp[s]:
                total = s + p
                if total >= 200:
                    if total < min_sum:
                        min_sum = total
                else:
                    if not new_dp[total]:
                        new_dp[total] = True
        dp = new_dp
    
    if min_sum == float('inf'):
        return min_single
    else:
        return min(min_single, min_sum - 50)
    
print(get_min_amount([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,
                          97,101,103,107,109,113,127,131,137,139,149]))