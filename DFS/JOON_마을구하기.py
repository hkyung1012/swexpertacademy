import sys
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

ans=0
dr,dc=[0,1,-1,0],[1,0,0,-1]
def dfs(r,c):
    cnt=1
    for i in range(4):
        nr,nc=r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<n and arr[nr][nc]==1:
            arr[nr][nc]=0
            cnt+=dfs(nr,nc)
    return cnt

ans=0
vil=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            ans+=1
            arr[i][j]=0
            vil.append(dfs(i,j))
#print(ans)
for x in sorted(vil):
    print(x)