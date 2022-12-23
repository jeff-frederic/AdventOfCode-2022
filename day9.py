
with open('day9.in') as f:
    lines = [l.strip().split(' ') for l in f.readlines()]

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, p):
        return abs(self.x - p.x), abs(self.y - p.y)

def solve(knots):
    tail_points = [Point()]
    points = [Point() for _ in range(knots)]

    for direction, i in lines:
        if direction in ['R', 'L']:
            move, dir_ = ('x', 1) if direction == 'R' else ('x', -1)
        if direction in ['U', 'D']:
            move, dir_ = ('y', 1) if direction == 'U' else ('y', -1)

        for j in range(int(i)):
            h = points[0]
            setattr(h, move, getattr(h, move) + 1*dir_)
            for k in range(1, knots):
                p = points[k]
                p_before = points[k-1]
                xd, yd = p_before.dist(p)
                if xd > 1 or yd > 1:
                    if p.x < p_before.x:
                        p.x += 1
                    elif p.x > p_before.x:
                        p.x -= 1
                    if p.y < p_before.y:
                        p.y += 1
                    elif p.y > p_before.y:
                        p.y -= 1
                    if k == len(points) - 1:
                        tail_points.append(Point(p.x, p.y))


    return len(set([(p.x, p.y) for p in tail_points]))

print("Answer to part 1: ", solve(2))
print("Answer to part 2: ", solve(10))