#LỚP POINT
import math

class Edge:
    def __init__ (this, points : list):
        this.points = points
        this.leng = len(points)

    def getEdge(this,  point1: int, point2: int):
        p1 = point1 * 2
        p2 = point2 * 2

        if p2 + 1 < this.leng and p1 + 1 < this.leng:
            return math.sqrt((this.points[p1] - this.points[p2])**2 + (this.points[p1 + 1] - this.points[p2 + 1])**2)
        
        return -1


datas = []
N = int(input())

for _ in range(N):
    datas.extend( [float(num) for num in input().split()] )

remote = Edge(datas)

for i in range(N):
    idx = i * 2
    e = remote.getEdge(idx, idx + 1)
    print("INVALID" if e < 0 else f'{round(e, 4):.4f}')