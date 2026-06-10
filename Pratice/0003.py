class tamgiac:
    def __init__ (self):
        self.A = self.B = self.C = (0, 0)
        self.AB = self.BC = self.CA = 0
        pass

    def add (self, points):
        self.A = points[0]
        self.B = points[1]
        self.C = points[2]

        self.AB = self.edge (self.A, self.B)
        self.BC = self.edge (self.B, self.C)
        self.CA = self.edge (self.C, self.A)

    def edge (self, p1, p2):
        return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

    def check (self):
        if self.AB + self.BC <= self.CA:
            return False
        elif self.BC + self.CA <= self.AB:
            return False
        elif self.CA + self.AB <= self.BC:
            return False
        else:
            return True
        
    def chuvi (self):
        if not self.check():
            return 'INVALID'

        return round( sum([self.AB, self.BC, self.CA]), 6 )


def main ():
    t = tamgiac()
    allTest = list()
    for _ in range(int(input())):
        data = list(map(int, input().split()))
        allTest.append( [(data[i], data[i + 1]) for i in range(0, len(data), 2)] )

    for test in allTest:
        t.add(test)
        print(t.chuvi())

if __name__ == "__main__":
    main()