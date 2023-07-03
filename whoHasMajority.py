class Solution:
    def majorityWins(self, arr, n, x, y):
        sm=min(x,y)
        xf,yf=0,0
        for i in arr:
            if i==x:
                xf+=1
            if i==y:
                yf+=1
        if xf==yf:
            return sm
        else:
            return (x if xf>yf else y)