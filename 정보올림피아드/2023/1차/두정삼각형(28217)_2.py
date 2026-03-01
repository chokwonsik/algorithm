n=int(input())
a=[]
b=[]
for i in range(n):
  a.append(list(map(int,input().split())))
for i in range(n):
  b.append(list(map(int,input().split())))

def ro(a):
  """120도 회전"""
  tmp=[[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(i+1):
      tmp[i][j]=a[n-1-j][i-j]
  return tmp

def sy(a):
  """좌우 대칭"""
  tmp=[[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(i+1):
      tmp[i][j]=a[i][i-j]
  return tmp

def cal(a,b):
  """A와 B의 차이를 계산"""
  cnt=0
  for i in range(n):
    for j in range(i+1):
      if a[i][j] != b[i][j]:
        cnt+=1
  return cnt

ans = float('inf')
"""A를 회전"""
for i in range(3):
  ans = min(ans, cal(a,b))
  a = ro(a)

"""A를 좌우 대칭 후 회전"""
a = sy(a)
for i in range(3):
  ans=min(ans,cal(a,b))
  a=ro(a)
print(ans)