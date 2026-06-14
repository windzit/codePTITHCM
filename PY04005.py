#LỚP TRIANGLE - 1
import math

class Edge: # Point bài trước cải thiện ở getEdge một tí
    def __init__ (this, points : list):
        this.points = points
        this.leng = len(points)

    def getEdge(this,  point1: int, point2: int):
        p1 = point1 * 2
        p2 = point2 * 2

        if p2 + 1 < this.leng and p1 + 1 < this.leng:
            return math.sqrt((this.points[p1] - this.points[p2])**2 + (this.points[p1 + 1] - this.points[p2 + 1])**2)
        
        return -1
    
class Triangle (Edge):
    def check(this, a, b , c):
        return (a + b + c) > ( max([a, b, c]) * 2 )

    def getPerimeter (this, index: int):
        idx = index * 3
        
        if idx + 5 >= this.leng:
            return -1
        
        a = this.getEdge(idx, idx + 1)
        b = this.getEdge(idx + 1, idx + 2) 
        c = this.getEdge(idx + 2, idx)
        
        if this.check (a, b, c):
            return a + b + c
        
        return -1


datas = []
N = int(input())

for _ in range(N):
    datas.extend( [float(num) for num in input().split()] )

remote = Triangle(datas)

for i in range(N):
    e = remote.getPerimeter(i)
    print("INVALID" if e < 0 else f'{round(e, 3):.3f}')