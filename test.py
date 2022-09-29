from vpython import *
import random

ball = sphere(pos = vector(-5,0,0), radius = 0.5, color = color.magenta, make_trail = True, retain = 100)
wallR = box(pos = vector(12,0,0), size = vector(0.4,24,24), color = color.blue)
wallL = box(pos = vector(-12,0,0), size = vector(0.4,24,24), color = color.blue)
wallBack = box(pos = vector(0,0,-12), size = vector(24,24,0.4), color = color.blue)
wallB = box(pos = vector(0,-12,0), size = vector(24,0.4,24), color = color.blue)
wallT = box(pos = vector(0,12,0), size = vector(24,0.4,24), color = color.blue)


ball.velocity = vector(25,5,-15)
deltat = 0.005
t = 0
ball.pos = ball.pos + ball.velocity * deltat
vscale = 0.05
varr = arrow(pos = ball.pos, axis = vscale * ball.velocity, color = color.yellow)

scene.autoscale = False

while t < 15:
    rate(200)

    ball.r = ball.radius - ball.radius
    wallThickness = 0.5
    ball.r = ball.r - wallThickness
    ball.pos = ball.pos + ball.velocity * deltat
    ballColor = [color.blue, color.green, color.magenta, color.yellow, color.red, color.cyan, color.black, color.orange, color.white]
    randomColor = random.choice(ballColor)

    t = t + deltat

    if ball.pos.x > (ball.r + wallR.pos.x) or (ball.pos.x + ball.r) <  wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
        ball.color = randomColor
        varr.color = randomColor
    elif ball.pos.y > (ball.r + wallT.pos.y) or (ball.pos.y + ball.r) < wallB.pos.y:
        ball.velocity.y = -ball.velocity.y
        ball.color = randomColor
        varr.color = randomColor
    if ball.pos.z > (ball.r + 12) or (ball.pos.z + ball.r) < -12:
        ball.velocity.z = -ball.velocity.z
        ball.color = randomColor
        varr.color = randomColor

    varr.pos = ball.pos
    varr.axis = vscale * ball.velocity
