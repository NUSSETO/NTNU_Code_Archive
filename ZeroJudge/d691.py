# ZeroJudge d691: Simply Subsets
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=d691

while True:
  try:
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    if a == b:
      print('A equals B.')
    elif a.issubset(b):
      print('A is a proper subset of B.')
    elif b.issubset(a):
      print('B is a proper subset of A.')
    elif a.intersection(b) != set():
      print('I \'m confused!')
    else:
      print('A and B are disjoint.')
  except:
    break # End of input
