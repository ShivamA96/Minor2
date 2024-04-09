import math
import random


WIDTH, HEIGHT = 800, 600
class Rectangle:
    def __init__(self,x, y, width, height, id= 0, density=0, velocity_x=0, velocity_y=0, force_x=0.0, force_y=0.0, color=(0, 0, 0), acceleration_x=0, acceleration_y=0):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity_x =  velocity_x
        self.velocity_y =  velocity_y
        self.force_x = force_x
        self.force_y = force_y
        self.density = density
        self.mass = self.density * self.width * self.height
        self.color  = color
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.w_counter = 0.0
        self.a_counter = 0.0
        self.s_counter = 0.0
        self.d_counter = 0.0


class Ellipse:
    def __init__(self, x, y, radius_x, radius_y, id= 0, density=0, velocity_x=0, velocity_y=0, force_x=0.0, force_y=0.0, color=(0, 0, 0), acceleration_x=0, acceleration_y=0):
        self.id = id
        self.x = x
        self.y = y
        self.width = radius_x
        self.height = radius_y
        self.velocity_x =  velocity_x
        self.velocity_y =  velocity_y
        self.force_x = force_x
        self.force_y = force_y
        self.density = density
        self.mass = math.pi * self.density * self.width * self.height
        self.color  = color
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.w_counter = 0.0
        self.a_counter = 0.0
        self.s_counter = 0.0
        self.d_counter = 0.0
        

def apply_force(object, force_x, force_y):
    object.acceleration_x += force_x / object.mass
    object.acceleration_y += force_y / object.mass
    
def force_by_player(object, force_x, force_y):

    object.force_x += force_x
    object.force_y += force_y
    
    object.acceleration_x += object.force_x  / object.mass
    object.acceleration_y += object.force_y / object.mass

    # object.force_x = 0
    # object.force_y = 0


    simulate_rigid_body_by_player(object)
    

# def collision_detection(object1, object2):
#     if isinstance(object1, Rectangle) and isinstance(object2, Rectangle):
#         return (abs(object1.x - object2.x) * 2 < (object1.width + object2.width)) and (abs(object1.y - object2.y) * 2 < (object1.height + object2.height))
#     elif isinstance(object1, Ellipse) and isinstance(object2, Ellipse):
#         dist_sq = (object1.x - object2.x) ** 2 / (object1.radius_x + object2.radius_x) ** 2 + (object1.y - object2.y) ** 2 / (object1.radius_y + object2.radius_y) ** 2
#         return dist_sq <= 1
#     else:
#         return False

def apply_acceleration(object, acceleration_x, acceleration_y):
    object.acceleration_x = acceleration_x
    object.acceleration_y = acceleration_y
    simulate_rigid_body_for_screen(object)
# def collision_response(object1, object2):
#     if collision_detection(object1, object2):
#         # Swap velocities
#         object1.velocity, object2.velocity = object2.velocity, object1.velocity

# def apply_gravity(object, gravity):
#     object.acceleration -= gravity

def apply_friction(object, friction):
    # object.acceleration_x = (friction * object.mass * 10)  / object.mass
    # object.acceleration_x -= object.acceleration_x * (friction)
    # apply_force(object, -(friction * object.mass * 10) , 0) 
    if object.velocity_x > 0:
        object.force_x -= (friction * object.mass * 10)
    elif object.velocity_x < 0:
        object.force_x += (friction * object.mass * 10)
    simulate_rigid_body(object)

    # object.velocity_y -= object.velocity_y * friction
    # a = (friction * object.mass * 10)  / object.mass \


def simulate_rigid_body_by_player(object):
    
    object.acceleration_x = object.force_x / object.mass
    object.acceleration_y = object.force_y / object.mass
    object.velocity_x += object.acceleration_x
    object.velocity_y += object.acceleration_y
    object.x += object.velocity_x
    object.y += object.velocity_y
    # object.force_x = 0
    # object.force_y = 0


def simulate_rigid_body(object):

    object.acceleration_x = object.force_x / object.mass
    object.acceleration_y = object.force_y / object.mass
    object.velocity_x += object.acceleration_x
    object.velocity_y += object.acceleration_y
    object.x += object.velocity_x
    object.y += object.velocity_y
    object.force_x = 0
    object.force_y = 0


def simulate_rigid_body_for_screen(object):
    # object.acceleration_x = object.force_x / object.mass
    # object.acceleration_y = object.force_y / object.mass
    object.velocity_x += object.acceleration_x
    object.velocity_y += object.acceleration_y
    object.x += object.velocity_x
    object.y += object.velocity_y
    object.force_x = 0
    object.force_y = 0

def create_object(ObjectType,id, x=0, y=0, radius_x=0, radius_y=0, color="RED"):
    print(id)
    if ObjectType == "E":
        # This is the Ellipse case
        color = random.choice(list(COLORS))
        x = random.randint(0, WIDTH - radius_x)
        y = random.randint(0, HEIGHT - radius_y)
        radius_x = random.randint(10, 50)
        radius_y = random.randint(10, 50)
        Object = Ellipse(x, y,  radius_x, radius_y, id, density= COLORS[color]["density"], color= COLORS[color]["rgb"])
        
    elif ObjectType == "R":
        # This is the Rectangle case
        color = random.choice(list(COLORS))
        radius_x = random.randint(10, 50)
        radius_y = random.randint(10, 50)
        x = random.randint(0, WIDTH - radius_x)
        y = random.randint(0, HEIGHT - radius_y)
        Object = Rectangle(x, y, radius_x, radius_y, id, density= COLORS[color]["density"], color= COLORS[color]["rgb"])

    return Object


def apply_force_on_object_by_player(object, force_x, force_y):

    force_by_player(object, force_x, force_y)

COLORS = {
    "RED": {"rgb": (255, 0, 0), "density": 0.01},
    "BLUE": {"rgb": (0, 255, 0),  "density": 0.02},
    "GREEN": {"rgb": (0, 0, 255),  "density": 0.03},
}
# import numpy as np

# def draw_shadow(screen, obj):
#     if isinstance(obj, Rectangle):
#         dx, dy = obj.x - LIGHT_SOURCE[0], obj.y - LIGHT_SOURCE[1]
#         shadow_polygon = [
#             (obj.x, obj.y + obj.height),
#             (obj.x + obj.width, obj.y + obj.height),
#             (obj.x + obj.width + dx, obj.y + dy),
#             (obj.x + dx, obj.y + dy),
#         ]
#     elif isinstance(obj, Ellipse):
#         theta = np.linspace(0, 2*np.pi, 100)
#         dx, dy = obj.x - LIGHT_SOURCE[0], obj.y - LIGHT_SOURCE[1]
#         shadow_polygon = [(obj.x + obj.width*np.cos(t) + dx, obj.y + obj.height*np.sin(t) + dy) for t in theta]

#     return shadow_polygon
# # In your main loop, draw the shadows before drawing the objects:
# LIGHT_SOURCE = (400, 300)


def globalCoordinates(objects):
    
    objParams = {}

    for obj in objects:
        # print(obj.id)
        objParams[obj.id] = (obj.x, obj.y, obj.width, obj.height)

        
    return objParams

    
def check_collision(obj1, obj2):
    x1, y1, width1, height1 = obj1
    x2, y2, width2, height2 = obj2
# TODO?: will this condition work for both ellipse and rectangle
    return (x1 < x2 + width2 and x1 + width1 > x2 and
            y1 < y2 + height2 and y1 + height1 > y2)

# TODO?: Efficient method of checking collisions
def check_all_collisions(objects):
    objParams = globalCoordinates(objects)
    collisions = []

    for id1, params1 in objParams.items():
        # print(id1, params1)
        for id2, params2 in objParams.items():
            # print(id2, params2)
            if id1 != id2 and check_collision(params1, params2):
                collisions.append((id1, id2))

    return collisions

def handle_collision(objects: list):
    collisions = check_all_collisions(objects)
     
    for i in collisions:
        a,b = i
        apply_force(objects[a-1], objects[a-1].force_x, -objects[a-1].force_y)
        simulate_rigid_body(objects[a-1])
        apply_force(objects[b-1], objects[b-1].force_x, -objects[b-1].force_y)
        simulate_rigid_body(objects[b-1])

def projectile_motion(object, initial_velocity, angle):
    # Convert angle to radians
    angle_rad = math.radians(angle)

    # Calculate velocities
    object.velocity_x = initial_velocity * math.cos(angle_rad)
    object.velocity_y = initial_velocity * math.sin(angle_rad) - (9.8 * 0.01)  # Gravity effect (9.8 m/s^2)

    # Update object position
    object.x += object.velocity_x
    object.y += object.velocity_y

    # Simulate rigid body motion
    simulate_rigid_body(object)