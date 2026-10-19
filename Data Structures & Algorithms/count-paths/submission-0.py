class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        f = [1]*(m+n+1)
        for i in range(1,m+n+1):
            f[i] = f[i-1]*i
        print(*f)
        return f[m+n-2]//(f[m-1]*(f[n-1]))
        # return 1
