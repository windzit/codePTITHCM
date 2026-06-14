#LỚP POINT
import math

class Edge:
    def __init__ (this, points : list):
        this.points = points
        this.leng = len(points)

    def getEdge(this, index : int):
        idx = index * 4

        if idx + 3 < this.leng:
            return math.hypot(this.points[idx] - this.points[idx + 2], this.points[idx + 1] - this.points[idx + 3])
        
        return -1


datas = []
N = int(input())

for _ in range(N):
    datas.extend( [float(num) for num in input().split()] )

remote = Edge(datas)

for i in range(N):
    e = remote.getEdge(i)
    print("INVALID" if e < 0 else f'{round(e, 4):.4f}')