def equilateral(sides):
    if triangle(sides):
        return sides[0] == sides[1] and sides[1] == sides[2]
    else:
        return False

def isosceles(sides):
    if triangle(sides):
        return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
    else:
        return False

def scalene(sides):
    if triangle(sides):
        return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]
    else:
        return False
    
def triangle(sides):
    return sides[0] > 0 and sides[1] > 0 and sides[2] > 0 and sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]