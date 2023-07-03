"""
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def myFun(p):
    return p.x
l=[Point(1,15),Point(10,5),Point(1,8)]
l.sort(key=myFun)
for i in l:
    print(i.x, i.y)
"""
#if you want to preserve the order
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lessthan__(self,other):
        return self.x < other.x
l=[Point(1,15),Point(10,5),Point(1,8)]
l.sort()
for i in l:
    print(i.x, i.y)