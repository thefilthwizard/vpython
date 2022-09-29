from vpython import *
import random


sun = sphere(pos = vector(0, 0, 0), color = color.orange, opacity=0.5, radius = 69.6340)
earth = sphere(pos = vector(sun.radius * 21.6, 0, 0), texture = textures.earth, radius = 6.375)
# planets
##earth = sphere(pos = vector(0, 0, 0), texture = textures.earth, radius = 6.375)

moon = sphere(pos = vector((earth.radius * 6) + earth.pos.x, 0, 0),
              texture = textures.rough,
              radius = 1.7371,
              axis = vector(0, 1, 0))

####sun = sphere(pos = vector((earth.radius * 234.24) + earth.pos.x, 0, 0),
####             color = color.orange,
####             opacity=0.5,
####             radius = 69.6000)
##
mercury = sphere(pos = vector(earth.pos.x - (earth.radius * 176.51), 0, 0),
                 texture = textures.metal,
                 radius = 2.4397)

venus = sphere(pos = vector(earth.pos.x - (earth.radius * 59.64), 0, 0),
                 texture = textures.granite,
                 radius = 6.0518)

mars = sphere(pos = vector(earth.pos.x + (earth.radius * 100.86), 0, 0),
              texture = textures.wood_old,
              radius = 3.3895)

jupiter = sphere(pos = vector(earth.pos.x + (earth.radius * 922.93), 0, 0),
              texture = textures.rock,
              radius = 6.9911)

##saturn = sphere(pos = vector(earth.pos.x - (earth.radius * 1883.53), 0, 0),
##              texture = textures.stucco,
##              radius = 5.8232)
##
##saturn.rings = ring(pos = vec(saturn.pos.x, saturn.pos.y, saturn.pos.z),
##                    axis = vec(0, 1, 0),
##                    size = vec(saturn.pos.x + 21.5, saturn.pos.x + 21.5, saturn.pos.x + 21.5),
##                    texture = textures.stones)
##
####uranus = sphere(pos = vector(earth.pos.x - (earth.radius * 1883.53), 0, 0),
####              texture = textures.stucco,
####              radius = 5.8232)
####
####neptune = sphere(pos = vector(earth.pos.x - (earth.radius * 1883.53), 0, 0),
####              texture = textures.stucco,
####              radius = 5.8232)


###orbital paths
moon.orbit = ring(pos = vec(earth.pos.x, earth.pos.y, earth.pos.z),
                  axis = vec(0, 1, 0),
                  color = color.white,
                  opacity=0.5,
                  radius = earth.radius * 6)
                  

earth.orbit = ring(pos = vec(sun.pos.x, 0, 0),
                   axis = vec(0, 1, 0),
                   size = vec(earth.pos.x * 2, earth.pos.x * 2, earth.pos.x * 2),
                   color = color.blue,
                   thickness = 2)

mercury.orbit = ring(pos = vec(sun.pos.x, 0, 0),
                  axis = vec(0, 1, 0),
                  size = vec((sun.pos.x * 2) - mercury.pos.x * 2, (sun.pos.x * 2) - mercury.pos.x * 2, (sun.pos.x * 2) - mercury.pos.x * 2),
                  color = color.white,
                  opacity = 0.5,
                  thickness = 2)

venus.orbit = ring(pos = vec(sun.pos.x, 0, 0),
                  axis = vec(0, 1, 0),
                  size = vec((sun.pos.x * 2) - venus.pos.x * 2, (sun.pos.x * 2) - venus.pos.x * 2, (sun.pos.x * 2) - venus.pos.x * 2),
                  color = color.cyan,
                  opacity = 0.5,
                  thickness = 2)

mars.orbit = ring(pos = vec(sun.pos.x, 0, 0),
                  axis = vec(0, 1, 0),
                  size = vec((sun.pos.x * 2) - mars.pos.x * 2, (sun.pos.x * 2) - mars.pos.x * 2, (sun.pos.x * 2) - mars.pos.x * 2),
                  color = color.red,
                  thickness = 2)

jupiter.orbit = ring(pos = vec(sun.pos.x, 0, 0),
                  axis = vec(0, 1, 0),
                  size = vec((sun.pos.x * 2) - jupiter.pos.x * 2, (sun.pos.x * 2) - jupiter.pos.x * 2, (sun.pos.x * 2) - jupiter.pos.x * 2),
                  color = color.yellow,
                  thickness = 5)

##saturn.orbit = ring(pos = vec(sun.pos.x, 0, 0),
##                  axis = vec(0, 1, 0),
##                  size = vec((sun.pos.x * 2) - saturn.pos.x * 2, (sun.pos.x * 2) - saturn.pos.x * 2, (sun.pos.x * 2) - saturn.pos.x * 2),
##                  color = color.green,
##                  thickness = 5)
##
####uranus.orbit = ring(pos = vec(sun.pos.x, 0, 0),
####                  axis = vec(0, 1, 0),
####                  size = vec((sun.pos.x * 2) - saturn.pos.x * 2, (sun.pos.x * 2) - saturn.pos.x * 2, (sun.pos.x * 2) - saturn.pos.x * 2),
####                  color = color.green)
####
####neptune.orbit = ring(pos = vec(sun.pos.x, 0, 0),
####                  axis = vec(0, 1, 0),
####                  size = vec((sun.pos.x * 2) - saturn.pos.x * 2, (sun.pos.x * 2) - saturn.pos.x * 2, (sun.pos.x * 2) - saturn.pos.x * 2),
####                  color = color.green)
##
### planet rotations and orbital rotations
##t = 0
##

while 0 == 0:
    rate(1)
##    # earth.rotate(angle = radians(360), axis=vector(1,0,0), origin = vector(0, 1, 0))
##    # t = t + 1
###
                  

    moon.rotate(angle = 0.21818181818181817, axis = vec(0, 1, 0), origin = vector(earth.pos.x, earth.pos.y, 0))
    #moon.orbit.rotate(angle = 0.9856262833675564, axis = vec(0, 1, 0), origin = vector(sun.pos.x, sun.pos.y, 0))
    earth.rotate(angle = 15.0, axis = vec(0, 1, 0), origin = vector(earth.pos.x, earth.pos.y, 0))
#    earth.year.rotate(angle = 0.9856262833675564, axis = vec(0, 1, 0), origin = vector(sun.pos.x, sun.pos.y, 0))
    #earth.orbit.rotate(angle = 0.9856262833675564, axis = vec(0, 1, 0), origin = vector(sun.pos.x, sun.pos.y, 0))
