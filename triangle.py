def equilateral(sides):
    a, b, c = sides
    return len(set(sides)) == 1 and is_positive(sides)


def isosceles(sides):
    a, b, c = sorted(sides)
    return len(set(sides)) <= 2 and is_positive(sides) and is_triangle(sides)
         

def scalene(sides):
    a, b, c = sorted(sides)
    return len(set(sides)) == 3 and is_positive(sides) and is_triangle(sides)

def is_positive(sides):
    a, b, c = sorted(sides)
    return a > 0

def is_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c 

    
