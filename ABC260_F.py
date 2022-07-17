import io
import sys

_INPUT = """\
6
2 3 5
1 3
1 4
1 5
2 4
2 5
3 2 4
1 4
1 5
2 5
3 5
4 5 9
3 5
1 8
3 7
1 9
4 6
2 7
4 8
1 7
2 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S,T,M=map(int,input().split())
  ss=[[] for _ in range(S)]
  d=dict()
  for i in range(M):
    u,v=map(int,input().split())
    ss[u-1].append(v-1-S)
  used=[[-1]*T for _ in range(T)]
  flg=0
  for k in range(S):
    if flg==1: break
    tmp=ss[k]
    for i in range(len(tmp)):
      if flg==1: break
      for j in range(i+1,len(tmp)):
        if used[min(tmp[i],tmp[j])][max(tmp[i],tmp[j])]==-1:
          used[min(tmp[i],tmp[j])][max(tmp[i],tmp[j])]=k
        else:
          flg=1
          print(used[min(tmp[i],tmp[j])][max(tmp[i],tmp[j])]+1,k+1,tmp[i]+1+S,tmp[j]+1+S)
          break
  if flg==0: print(-1)