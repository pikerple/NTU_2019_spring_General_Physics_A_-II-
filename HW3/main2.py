from vpython import *

d=0.5 # g = 9.8 m/s^2
size = 0.5# ball radius = 0.25 m
height = 15.0 # ball center initial height = 15 m
spheres = {}
location = {}
arrows = {}
scene = canvas(width=800, height=800, center =vec(0,height/2,0), background=vec(0.5,0.5,0)) # open a window
for x in range (0, 31):
    for y in range (0, 31):
        z = 0
        location[(x, y)] = z
for x in range (1, 30):
    for y in range (1, 30):
        arrows[(x, y)]=arrow(pos = vec(x,y,0),shaftwidth = 0.1)
location[(0, 30)] = 3
location[(30, 30)] = -6
location[(30, 0)] = -9
location[(0, 0)] = 0
for x in range (1, 30):
        location[(x, 0)] = location[(0,0)]
        location[(x, 30)]= location[(0,30)]
for y in range (1, 30):
        location[(0, y)] = location[(30,0)]
        location[(30, y)] = location[(30,30)]

for c in range (1,1000):
    for x in range (1, 30):
        for y in range (1, 30):
            tmpvx =(location[(x+1,y)] - location[(x-1,y)])/2/d
            tmpvy =(location[(x,y+1)] - location[(x,y-1)])/2/d
            tmp = ((location[(x+1,y)] + location[(x-1,y)] + location[(x,y+1)] + location[(x,y-1)]))/4
            location[(x, y)]= tmp
            arrows[(x, y)].axis= vec(-tmpvx,-tmpvy,0)
    