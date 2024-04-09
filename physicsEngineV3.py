import turtle
class Objects:
    def __init__(self,type,x, y, width, height, id= 0, density=0, velocity_x=0, velocity_y=0, force_x=0.0, force_y=0.0, color=(0, 0, 0), acceleration_x=0, acceleration_y=0):
        self.type = type
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
    
    def apply_force_x(object, force_x):
        object.acceleration_x += force_x / object.mass
    
    def apply_force_y(object, force_y):
        object.acceleration_y += force_y / object.mass


# TODO: SEPARATE V2 functions
    







