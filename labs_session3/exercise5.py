def is_inside(pt, rect):
    x, y = pt
    a, b, width, height = rect
    if a < x < a + width and b < y < b + height:
        return True
    return False

pt = list(map(int, input('input a location: ').split()))
rect = list(map(int, input('input a loction, width and high: ').split()))

print(is_inside(pt,rect))
