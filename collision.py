import pygame
from physicsEngine import Rectangle,Ellipse, simulate_rigid_body,apply_acceleration, apply_friction, apply_force, force_by_player, create_object,handle_collision
from physicsEngine import COLORS as COLORS
import random
WIDTH, HEIGHT = 800, 600
GRAVITY = 0.98
COR = 0.9

pygame.init()
# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a Rectangle object for the platform
platform = Rectangle(0, HEIGHT - 10, WIDTH, 10)
walls = [Rectangle(0, 0, 10, HEIGHT), Rectangle(WIDTH - 10, 0, 10, HEIGHT)]




clock=pygame.time.Clock()
FPS = 100

# Main game loop
running = True
dragging = False




# def create_object(ObjectType = "R", x=0, y=0, radius_x=0, radius_y=0, color="RED"):

#     if ObjectType == "E":
#         # This is the Ellipse case
#         color = random.choice(list(COLORS))
#         x = random.randint(0, WIDTH - radius_x)
#         y = random.randint(0, HEIGHT - radius_y)
#         radius_x = random.randint(10, 50)
#         radius_y = random.randint(10, 50)
#         Object = Ellipse(x, y, radius_x, radius_y, density= COLORS[color]["density"], color= COLORS[color]["rgb"])
        
#     elif ObjectType == "R":
#         # This is the Rectangle case
#         color = random.choice(list(COLORS))
#         radius_x = random.randint(10, 50)
#         radius_y = random.randint(10, 50)
#         x = random.randint(0, WIDTH - radius_x)
#         y = random.randint(0, HEIGHT - radius_y)
#         Object = Rectangle(x, y, radius_x, radius_y, density= COLORS[color]["density"], color= COLORS[color]["rgb"])

#     return Object



def pygameStart():
    selected_obj = None  # No object is selected initially

    objects = [create_object("E", 1)]

    running = True


    while running:


        screen.fill((255, 255, 255))

        # Draw the platform
        pygame.draw.rect(screen, (0, 255, 0), (platform.x, platform.y, platform.width, platform.height))
        pygame.draw.rect(screen, (0, 255, 0), (walls[0].x, walls[0].y, walls[0].width, walls[0].height))
        pygame.draw.rect(screen, (0, 255, 0), (walls[1].x, walls[1].y, walls[1].width, walls[1].height))

        # print(objects[0].__class__.__name__)
        for i in objects:
            
                # print(i.color)
            if i.__class__.__name__ == "Rectangle":
                pygame.draw.rect(screen, i.color, (i.x, i.y, i.width, i.height))
            elif i.__class__.__name__ == "Ellipse":
                rect = pygame.Rect(i.x, i.y, i.width, i.height)
                pygame.draw.ellipse(screen, i.color, rect)


        # for obj in objects:

        handle_collision(objects)

            
        

        for obj in objects:

            

            # APPLY GRAVITY
            apply_acceleration(obj, 0, GRAVITY)

            simulate_rigid_body(obj)

            # FAKE FRICTION

            if obj.y + obj.height == platform.y  and obj.velocity_y < 0: 
                
                # print(obj.velocity_y, obj.mass)
                obj.acceleration_x -= obj.velocity_x * 0.1
                # # print(obj.acceleration_x, obj.acceleration_y)
                # simulate_rigid_body(obj)
                # apply_friction(obj, 1)
            # BOUNCE
            if obj.y + obj.height > platform.y:
                obj.y = platform.y - obj.height 
                obj.velocity_y *= -COR

 

            # WALLS COLLISION

            if ((obj.x < walls[0].x + walls[0].width and obj.x + obj.width > walls[0].x and obj.y < walls[0].y + walls[0].height and obj.y + obj.height > walls[0].y) or
                (obj.x < walls[1].x + walls[1].width and obj.x + obj.width > walls[1].x and obj.y < walls[1].y + walls[1].height and obj.y + obj.height > walls[1].y)):
                if(obj.x < walls[0].x + walls[0].width and obj.x + obj.width > walls[0].x and obj.y < walls[0].y + walls[0].height and obj.y + obj.height > walls[0].y):
                    obj.x = walls[0].x + walls[0].width
                elif(obj.x < walls[1].x + walls[1].width and obj.x + obj.width > walls[1].x and obj.y < walls[1].y + walls[1].height and obj.y + obj.height > walls[1].y):
                    obj.x = walls[1].x - obj.width
                obj.velocity_x = -obj.velocity_x
     


        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse is over an object
                mouse_pos = pygame.mouse.get_pos()
                for obj in objects:
                    if obj.x < mouse_pos[0] < obj.x + obj.width and obj.y < mouse_pos[1] < obj.y + obj.height:
                        selected_obj = obj  # Select the object
                        break

        # Get the state of the keys
        keys = pygame.key.get_pressed()
        #TODO? : WHY IS DDD AND A COMBINATION NOT WORKING as expected!?
        if keys[pygame.K_w] and selected_obj:

            selected_obj.w_counter += 0.5
            selected_obj.force_y = 0
            # apply_force(selected_obj, 0, -GRAVITY+10)
            force_by_player(selected_obj, 0, -selected_obj.w_counter)
            selected_obj.a_counter = 0.0
            selected_obj.s_counter = 0.0
            selected_obj.d_counter = 0.0
            # selected_obj.y -= 10  # Move up
        if keys[pygame.K_a] and selected_obj:
            selected_obj.a_counter += 0.1            
            selected_obj.force_x = 0
            force_by_player(selected_obj, -selected_obj.a_counter, 0)

            selected_obj.w_counter = 0
            selected_obj.s_counter = 0
            selected_obj.d_counter = 0

        if keys[pygame.K_s] and selected_obj:
            selected_obj.s_counter += 0.5
            selected_obj.force_y = 0
            
            force_by_player(selected_obj, 0, selected_obj.s_counter)

            selected_obj.d_counter = 0
            selected_obj.w_counter = 0
            selected_obj.a_counter = 0

        if keys[pygame.K_d] and selected_obj:
            selected_obj.d_counter += 0.1
            selected_obj.force_x = 0
            
            force_by_player(selected_obj, selected_obj.d_counter, 0)

            selected_obj.w_counter = 0
            selected_obj.a_counter = 0
            selected_obj.s_counter = 0

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":

    pygameStart()