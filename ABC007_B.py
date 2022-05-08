import io
import sys

_INPUT = """\
6
xyz
c
a
aaaaa
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A=input()
  if A=='a': print(-1)
  else: print('a')