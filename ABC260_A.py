import io
import sys

_INPUT = """\
6
pop
abc
xxx
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  flg=0
  for i in range(3):
    if S.count(S[i])==1: print(S[i]); flg=1; break
  if flg==0: print(-1)