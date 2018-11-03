
def matrix(a):
    n=len(a)-1
    m=[[0 for i in range(n + 1)] for j in range(n+ 1)]
    s= [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(1,n+1):
        m[i][i]=0
    for r in range(2,n+1):
        for i  in range(n-r+1+1):
            j= i+r-1
            m[i][j]=m[i+1][j]+a[i-1]*a[i]*a[j]
            s[i][j]=i
            for k in range(i+1,j):
                t=m[k+1][j]+m[i][k]+a[i-1]*a[k]*a[j]
                if t<m[i][j]:
                    m[i][j]=t
                    s[i][j]=k
    return m,s

a=[1,2,3,1,2,3]
print(matrix(a)[0])
print(matrix(a)[1])

