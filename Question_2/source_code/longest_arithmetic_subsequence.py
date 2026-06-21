def longest_arithmetic_subsequence(arr):
    n = len(arr)

    if n <= 1:
        return n

    dp = [dict() for _ in range(n)]
    ans = 2

    for i in range(n):
        for j in range(i):
            diff = arr[i] - arr[j]
            dp[i][diff] = dp[j].get(diff, 1) + 1
            ans = max(ans, dp[i][diff])

    return ans

arr = [3, 6, 9, 12, 15]
print("Length =", longest_arithmetic_subsequence(arr))
