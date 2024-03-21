class Rectangle:
    def __init__(self, x, y, width, height, mass=0, density=0, velocity_x=0, velocity_y=0, force_x=0, force_y=0, color=(0, 0, 0), acceleration_x=0, acceleration_y=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity_x =  velocity_x
        self.velocity_y =  velocity_y
        self.force_x = force_x
        self.force_y = force_y
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.mass = mass
        self.density = density
        self.color  = color

class Ellipse:
    def __init__(self, x, y, radius_x, radius_y, mass=0, density=0, velocity_x=0, velocity_y=0, force_x=0, force_y=0, color=(0, 0, 0), acceleration_x=0, acceleration_y=0):
        self.x = x
        self.y = y
        self.radius_x = radius_x
        self.radius_y = radius_y
        self.velocity_x =  velocity_x
        self.velocity_y =  velocity_y
        self.force_x = force_x
        self.force_y = force_y
        self.mass = mass
        self.density = density
        self.color  = color
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        # self.color  = color

def apply_force(object, force_x, force_y):
    object.acceleration_x += force_x / object.mass
    object.acceleration_y += force_y / object.mass
    
def collision_detection(object1, object2):
    if isinstance(object1, Rectangle) and isinstance(object2, Rectangle):
        return (abs(object1.x - object2.x) * 2 < (object1.width + object2.width)) and (abs(object1.y - object2.y) * 2 < (object1.height + object2.height))
    elif isinstance(object1, Ellipse) and isinstance(object2, Ellipse):
        dist_sq = (object1.x - object2.x) ** 2 / (object1.radius_x + object2.radius_x) ** 2 + (object1.y - object2.y) ** 2 / (object1.radius_y + object2.radius_y) ** 2
        return dist_sq <= 1
    else:
        return False

def apply_acceleration(object, acceleration_x, acceleration_y):
    object.acceleration_x = acceleration_x
    object.acceleration_y = acceleration_y

def collision_response(object1, object2):
    if collision_detection(object1, object2):
        # Swap velocities
        object1.velocity, object2.velocity = object2.velocity, object1.velocity

def apply_gravity(object, gravity):
    object.acceleration -= gravity

def apply_friction(object, friction):
    object.acceleration -= object.velocity * friction

def simulate_rigid_body(object):
    object.velocity_x += object.acceleration_x
    object.velocity_y += object.acceleration_y
    if isinstance(object, Rectangle):
        object.x += object.velocity_x
        object.y += object.velocity_y
    elif isinstance(object, Ellipse):
        object.x += object.velocity_x
        object.y += object.velocity_y
    object.force_x = 0
    object.force_y = 0

def ray_casting(object, target):
    # For simplicity, let's assume the ray is cast from the object's position to the right
    if isinstance(object, Rectangle) and isinstance(target, Rectangle):
        return object.x <= target.x <= object.x + object.width and object.y <= target.y <= object.y + object.height
    elif isinstance(object, Ellipse) and isinstance(target, Ellipse):
        dist_sq = (object.x - target.x) ** 2 / object.radius_x ** 2 + (object.y - target.y) ** 2 / object.radius_y ** 2
        return dist_sq <= 1
    else:
        return False