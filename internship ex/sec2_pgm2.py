def nearest_same_x_or_y(points,x,y):
    min_dist=float('inf')
    neareset=None
    for px,py in points:
        if px==x or py==y:
            dist=(px-x)**2+(py-y)**2
            if dist<min_dist:
                min_dist=dist
                neareset=(px,py)
    return neareset
points = [(1,2),(3,4),(3,2),(5,2)]
x,y=3,3
print(nearest_same_x_or_y(points,x,y))
