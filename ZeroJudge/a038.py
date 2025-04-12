# ZeroJudge a038: Reversed numbers
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a038

n = int(input())

if n == 0: # No need to reverse
  print(n) 

while n%10 == 0: # 0 cannot be in first position after reversing
  n //= 10

while n != 0:
  print(n%10, end = '')
  n //= 10
