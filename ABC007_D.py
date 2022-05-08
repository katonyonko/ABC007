import io
import sys

_INPUT = """\
6
1 9
40 49
1 1000
1 1000000000000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B=input().split()
  def res(k):
    if k=='0': return 0
    dp=[[0]*2 for _ in range(len(k)+1)]
    for i in range(len(k)):
      dp[i+1][0]=dp[i][0]*10
      if i>0: dp[i+1][0]+=(int(k[:i])-dp[i][0])*2
      if dp[i][1]==1: dp[i+1][0]+=int(k[i])
      elif int(k[i])>4: dp[i+1][0]+=1
      if dp[i][1]==1 or int(k[i])==4 or int(k[i])==9: dp[i+1][1]=1
    return sum(dp[-1])
  print(res(B)-res(str(int(A)-1)))