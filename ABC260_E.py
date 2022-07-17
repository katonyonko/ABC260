import io
import sys

_INPUT = """\
6
3 5
1 3
1 4
2 5
1 2
1 2
5 9
1 5
1 7
5 6
5 8
2 6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #BIT(Binary Indexed Tree, Fenwick Treeとも, 添え字が0から始まる形で管理していることに注意)
  class BIT:
      def __init__(self, n):
          self._n = n
          self.data = [0] * n
      def add(self, p, x):
          assert 0 <= p < self._n
          p += 1
          while p <= self._n:
              self.data[p - 1] += x
              p += p & -p
      #合計にはrを含まない
      def sum(self, l, r):
          assert 0 <= l <= r <= self._n
          return self._sum(r) - self._sum(l)
      def _sum(self, r):
          s = 0
          while r > 0:
              s += self.data[r - 1]
              r -= r & -r
          return s

  from collections import defaultdict
  N,M=map(int,input().split())
  tmp=[list(map(lambda x: int(x)-1,input().split())) for _ in range(N)]
  d=defaultdict(int)
  for i in range(N):
    A,B=tmp[i]
    d[A]=max(d[A],B)
  bit=BIT(M+1)
  t=max([tmp[i][0] for i in range(N)])+1
  t2=min([tmp[i][1] for i in range(N)])
  bit.add(t,1)
  for i in range(M):
    if i==t2: break
    t=max(t,d[i]+1)
    bit.add(t-i-1,1)
    bit.add(M-i,-1)
  print(*[bit.sum(0,i+2) for i in range(M)])