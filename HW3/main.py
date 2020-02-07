from vpython import *

d=0.01 # g = 9.8 m/s^2
size = 0.5# ball radius = 0.25 m
height = 15.0 # ball center initial height = 15 m
spheres = {}
location = {}
arrows = {}
#scene = canvas(color = white,width=800, height=800, center =vec(0,height/2,0), background=vec(0.5,0.5,0)) # open a window
for x in range (0, 31):
    for y in range (0, 31):
        z = 0
        spheres[(x, y)] = sphere(radius = size, color=color.red)
        spheres[(x, y)].pos = vec(x,y,z)
        location[(x, y)] = z

location[(0, 0)] = 5
location[(0, 30)] = -10
location[(30, 30)] = -15
location[(30, 0)] = 0
for x in range (1, 30):
        location[(x, 0)] = location[(30,0)]
        location[(x, 30)]= location[(0,30)]
for y in range (1, 30):
        location[(0, y)] = location[(0,0)]
        location[(30, y)] = location[(30,30)]
for c in range (1,1000):
    for x in range (1, 30):
        for y in range (1, 30):
            tmp = ((location[(x+1,y)] + location[(x-1,y)] + location[(x,y+1)] + location[(x,y-1)]))/4
            location[(x, y)]= tmp
    for x in range (0, 31):
        for y in range (0, 31):
            z = 0
            spheres[(x, y)].pos = vec(x,y,location[(x,y)]) 
            

  	
