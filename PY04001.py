#LỚP POINT
class Edge:
    def addPoint(self):
        x1, y1, x2, y2 = map(float, input().split())
        self.p1, self.p2 = [x1, y1], [x2, y2]

    def getEdge(self):
        # math.hypot(self.p1[0] - self.p2[0], self.p1[1] - self.p2[1])
        return ((self.p1[0] - self.p2[0])**2 + (self.p1[1] - self.p2[1])**2) ** 0.5
    

remote = Edge()
for _ in range(int(input())):
    remote.addPoint()
    print(f"{remote.getEdge():.4f}")