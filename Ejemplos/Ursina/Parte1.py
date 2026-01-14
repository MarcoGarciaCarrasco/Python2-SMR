from ursina import *

app = Ursina()

top_wall = Entity(model="quad" , scale=(10,0.2), position = (0,4,0), color = color.blue, collider="box") 
botton_wall = Entity(model="quad" , scale=(10,0.2), position = (0,-4,0), color = color.blue, collider="box") 
left_wall = Entity(model="quad" , scale=(0.2,10), position = (-5,0,0), color = color.blue, collider="box") 
right_wall = Entity(model="quad" , scale=(0.2,10), position = (5,0,0), color = color.blue, collider="box") 

ball = Entity(model="circle", color = color.orange, scale= 0.3, position = (0,0,0), collider = "box")

direction = 6.7

def update():
    global direction

    ball.x += direction* time.dt

    if ball.intersects(right_wall).hit or ball.intersects(left_wall).hit:

        direction *= -1

app.run()