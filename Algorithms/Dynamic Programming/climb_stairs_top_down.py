def climbStairs(n, memo={}):
    if n == 1:
        return 1

    if n not in memo:
        memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)

    return memo[n]
