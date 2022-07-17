import io
import sys

_INPUT = """\
6
4 2
OXXX
XXXX
XXXX
XXXX
6
1 1
1 4
2 2
2 3
3 1
4 4
5 10
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO
5
1 1
2 3
3 4
4 2
5 5
8 5
OXXOXXOX
XOXXOXOX
XOOXOOXO
OXOOXOXO
OXXOXXOX
XOXXOXOX
XOOXOOXO
OXOOXOXO
6
7 2
8 1
4 5
8 8
3 4
1 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  S=[input() for _ in range(N)]