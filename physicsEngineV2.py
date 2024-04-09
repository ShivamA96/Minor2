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



    simulate_rigid_body_by_player(object)
def force_by_player(object, force_x, force_y):

    object.force_x += force_x
    object.force_y += force_y
    
    object.acceleration_x += object.force_x  / object.mass
    object.acceleration_y += object.force_y / object.mass



    simulate_rigid_body_by_player(object)



def apply_acceleration(object, acceleration_x, acceleration_y):
    object.acceleration_x = acceleration_x
    object.acceleration_y = acceleration_y
    simulate_rigid_body_for_screen(object)

def apply_friction(object, friction):

    if object.force_x > 0:
        # object.force_x -= (10 * friction * object.mass)
        object.force_x -= (friction * object.force_x )
        simulate_rigid_body(object)

    elif object.force_x < 0:
        object.force_x += (friction * -object.force_x)
        simulate_rigid_body(object)

    print(object.velocity_x, object.force_x)


def simulate_rigid_body_by_player(object):
    
    object.acceleration_x += object.force_x / object.mass
    object.acceleration_y += object.force_y / object.mass
    object.velocity_x += object.acceleration_x
    object.velocity_y += object.acceleration_y
    object.x += object.velocity_x
    object.y += object.velocity_y


def simulate_rigid_body(object):

    object.acceleration_x += object.force_x / object.mass
    object.acceleration_y += object.force_y / object.mass
    object.velocity_x += object.acceleration_x
    object.velocity_y += object.acceleration_y
    object.x += object.velocity_x
    object.y += object.velocity_y
    # object.force_x = 0
    # object.force_y = 0


def simulate_rigid_body_x(object):

    object.acceleration_x += object.force_x / object.mass
    # object.acceleration_y += object.force_y / object.mass
    object.velocity_x += object.acceleration_x
    # object.velocity_y += object.acceleration_y
    object.x += object.velocity_x
    # object.y += object.velocity_y

def simulate_rigid_body_y(object):
    
        # object.acceleration_x += object.force_x / object.mass
        object.acceleration_y += object.force_y / object.mass
        # object.velocity_x += object.acceleration_x
        object.velocity_y += object.acceleration_y
        # object.x += object.velocity_x
        object.y += object.velocity_y


def simulate_rigid_body_for_screen(object):

    object.velocity_x += object.acceleration_x
    object.velocity_y += object.acceleration_y
    object.x += object.velocity_x
    object.y += object.velocity_y
    # object.force_x = 0
    # object.force_y = 0

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



    