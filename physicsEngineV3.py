import math


class PyEn:
    """
    PyEn class represents a physics engine object.

    Attributes:
        type (str): The type of the object.
        x (float): The x-coordinate of the object.
        y (float): The y-coordinate of the object.
        width (float): The width of the object.
        height (float): The height of the object.
        density (float, optional): The density of the object. Default is 1.
        id (int, optional): The ID of the object. Default is 0.
        velocity_x (float, optional): The velocity in the x-direction. Default is 0.
        velocity_y (float, optional): The velocity in the y-direction. Default is 0.
        force_x (float, optional): The force in the x-direction. Default is 0.0.
        force_y (float, optional): The force in the y-direction. Default is 0.0.
        color (tuple, optional): The color of the object in RGB format. Default is (0, 0, 0).
        acceleration_x (float, optional): The acceleration in the x-direction. Default is 0.
        acceleration_y (float, optional): The acceleration in the y-direction. Default is 0.
        w_counter (float): A counter for the 'w' key.
        a_counter (float): A counter for the 'a' key.
        s_counter (float): A counter for the 's' key.
        d_counter (float): A counter for the 'd' key.
    """
    def __init__(self,type,x, y, width, height,  density=1,id =0, velocity_x=0, velocity_y=0, force_x=0.0, force_y=0.0, color=(0, 0, 0), acceleration_x=0, acceleration_y=0):
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
        self.mass = (self.density * self.width * self.height )/10
        self.color  = color
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.w_counter = 0.0
        self.a_counter = 0.0
        self.s_counter = 0.0
        self.d_counter = 0.0

    def simulate_rigid_body_for_screen_x(self):
        self.velocity_x += self.acceleration_x

        self.x += self.velocity_x / 100

            # self.force_x = 0
    def apply_acceleration_x(self, acceleration_x):
        self.acceleration_x = acceleration_x
        # self.simulate_rigid_body_for_screen_x()
            
    def apply_acceleration_y(self, acceleration_y):
        self.acceleration_y = acceleration_y
        # self.simulate_rigid_body_for_screen_y()



    def simulate_rigid_body_for_screen_y(self):
        self.velocity_y += self.acceleration_y

        self.y += self.velocity_y / 100 

    
    def apply_force_x(self, force_x):
        self.acceleration_x += force_x / self.mass

    def apply_force_y(self, force_y):
        self.acceleration_y += force_y / self.mass


    def simulate_rigid_body_x(self):

        self.acceleration_x += self.force_x / self.mass
        # self.acceleration_y += self.force_y / self.mass
        self.velocity_x += self.acceleration_x * 0.01
        # self.velocity_y += self.acceleration_y
        self.x += 0.5 * self.acceleration_x * 0.01 ** 2 + self.velocity_x * 0.01

        self.force_x = 0


        # def simulate_rigid_body_x(self):

        # self.acceleration_x += self.force_x / self.mass
        # # self.acceleration_y += self.force_y / self.mass
        # self.velocity_x += self.acceleration_x * 0.01
        # # self.velocity_y += self.acceleration_y
        # self.x += 0.5 * self.acceleration_x * 0.01 ** 2 + self.velocity_x * 0.01

        # self.force_x = 0

    def simulate_rigid_body_y(self):
        
            # self.acceleration_x += self.force_x / self.mass
            # self.acceleration_y += self.force_y / self.mass
            # # self.velocity_x += self.acceleration_x
            # self.velocity_y += self.acceleration_y 
            # # self.x += self.velocity_x
            # self.y += self.velocity_y / 100

            # self.force_y = 0

        # self.force_x = 0


        # self.force_y = 0

        self.acceleration_y += self.force_y / self.mass
        # self.acceleration_y += self.force_y / self.mass
        self.velocity_y += self.acceleration_y * 0.01
        # self.velocity_y += self.acceleration_y
        self.y += 0.5 * self.acceleration_y * 0.01 ** 2 + self.velocity_y * 0.01

        self.force_y = 0

        

    def simulate_rigid_body_by_player_x(self):
        
        self.acceleration_x += self.force_x / self.mass
        # self.acceleration_y += self.force_y / self.mass
        self.velocity_x += self.acceleration_x
        # self.velocity_y += self.acceleration_y
        self.x += self.velocity_x / 100
        # self.y += self.velocity_y

    def simulate_rigid_body_by_player_y(self):
        
        # self.acceleration_x += self.force_x / self.mass
        self.acceleration_y += self.force_y / self.mass
        # self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y
        # self.x += self.velocity_x
        self.y += self.velocity_y / 100
    def force_by_player_x(self,  force_x):

        self.force_x = force_x
        # self.acceleration_x += self.force_x  / self.mass

        # self.simulate_rigid_body_by_player_x()
        
    def force_by_player_y(self,  force_y):
        
        self.force_y = force_y
        # self.acceleration_y += self.force_y / self.mass

        # self.simulate_rigid_body_by_player_y()
        
    def globalCoordinates(self, objects):
    
        objParams = {}

        for obj in objects:
            # print(obj.id)
            objParams[obj.id] = (obj.x, obj.y, obj.width, obj.height)

            
        return objParams

        
    def check_collision(self, obj1, obj2):
        x1, y1, width1, height1 = obj1
        x2, y2, width2, height2 = obj2
    # TODO?: will this condition work for both ellipse and rectangle
        return (x1 < x2 + width2 and x1 + width1 > x2 and
                y1 < y2 + height2 and y1 + height1 > y2)

    # TODO?: Efficient method of checking collisions
    def check_all_collisions(self, objects):
        objParams = self.globalCoordinates(objects)
        collisions = []

        for id1, params1 in objParams.items():
            # print(id1, params1)
            for id2, params2 in objParams.items():
                # print(id2, params2)
                if id1 != id2 and self.check_collision(params1, params2):
                    collisions.append((id1, id2))

        return collisions

    def handle_collision(self, objects: list):
        collisions = self.check_all_collisions(objects)
        
        for i in collisions:
            a,b = i
            # object(apply_force(objects[a-1], objects[a-1].force_x, -objects[a-1].force_y)
            # self.simulate_rigid_body(objects[a-1])
            # self.apply_force(objects[b-1], objects[b-1].force_x, -objects[b-1].force_y)
            # self.simulate_rigid_body(objects[b-1])

            self.apply_force_x(objects[a-1], objects[a-1].force_x)
            # self.simulate_rigid_body_x(objects[a-1]) 
            self.apply_force_x(objects[b-1], objects[b-1].force_x)
            # self.simulate_rigid_body_x(objects[b-1])
            self.apply_force_x(objects[a-1], objects[a-1].force_x)
            # self.simulate_rigid_body_x(objects[a-1])
            self.apply_force_y(objects[b-1], objects[b-1].force_y)
            # self.simulate_rigid_body_y(objects[b-1])
            

    def apply_friction(self,  friction):
            
            if self.force_x < (friction * self.mass) and self.force_x > -((friction * self.mass)):
                # print(self.velocity_x, "1st condition")
                self.velocity_x = 0
                self.simulate_rigid_body_by_player_x()
                # self.simulate_rigid_body_x()
            

                # self.force_x -= (10 * friction * self.mass)
            elif self.force_x > (friction * self.mass) :
                self.force_x -= (friction * self.mass)
                # print(self.force_x, "1")
                
                # self.simulate_rigid_body_x()
    
            elif self.force_x < -(friction * self.mass):
                self.force_x += (friction * self.mass)
                # print(self.force_x, "2")
                # self.simulate_rigid_body_x()



            # print(self.id, self.force_x)

    def projectile_motion(self,  initial_velocity, angle):
        self.velocity_x = initial_velocity * math.cos(angle)
        self.velocity_y = initial_velocity * math.sin(angle) - (9.8 * 0.01)
        self.x += self.velocity_x
        self.y += self.velocity_y

  