import math


class Solver:
    def demo(self, a, b, c):

        d = b ** 2 - 4 * a * c
        print('a=%d b=%d c=%d d=%d'%(a, b, c, d))
        if d >= 0:

            disc = math.sqrt(d)

            root1 = (-b + disc) / (2 * a)

            root2 = (-b - disc) / (2 * a)

            print(root1, root2)

        else:

            raise Exception

    def ddumy(self, a, b):
        return a + b


Solver().demo(2, 3, 0)
print(Solver().ddumy(2, 1))