import io
import sys

_INPUT = """\
6
2 3 4
1 5 5
10 5 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,X,Y=map(int,input().split())
  dp=[[0]*2 for _ in range(N)]
  dp[0][0]=1
  for i in range(N-1):
    dp[i+1][0]+=dp[i][0]
    dp[i][1]+=dp[i][0]*X
    dp[i+1][0]+=dp[i][1]
    dp[i+1][1]+=dp[i][1]*Y
  print(dp[-1][1])