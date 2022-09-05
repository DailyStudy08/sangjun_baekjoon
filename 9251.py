import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = input().strip()
m = input().strip()
dp = [[0 for _ in range(len(n)+1)]for _ in range(len(m)+1)] 
for i in range(1, len(m)+1):
    for j in range(1, len(n)+1):
        if n[j-1] == m[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])