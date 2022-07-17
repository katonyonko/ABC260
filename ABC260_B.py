import io
import sys

_INPUT = """\
6
6 1 0 2
80 60 80 60 70 70
40 20 50 90 90 80
5 2 1 2
0 100 0 100 0
0 0 100 100 0
15 4 3 2
30 65 20 95 100 45 70 85 20 35 95 50 40 15 85
0 25 45 35 65 70 80 90 40 55 20 20 45 75 100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,X,Y,Z=map(int,input().split())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  ans=[]
  tmp=[(i+1,A[i],B[i],A[i]+B[i]) for i in range(N)]
  tmp.sort(key=lambda x: (-x[1], x[0]))
  ans=tmp[:X]
  tmp=tmp[X:]
  tmp.sort(key=lambda x: (-x[2], x[0]))
  ans=ans+tmp[:Y]
  tmp=tmp[Y:]
  tmp.sort(key=lambda x: (-x[3], x[0]))
  ans=ans+tmp[:Z]
  tmp=tmp[Z:]
  ans=sorted([ans[i][0] for i in range(X+Y+Z)])
  print(*ans,sep='\n')