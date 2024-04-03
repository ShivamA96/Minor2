import pygame
from physicsEngine import Rectangle,Ellipse, apply_force, simulate_rigid_body,apply_acceleration, apply_friction
from pygame import gfxdraw
# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
GRAVITY = 0.98
COR = 0.5

import random
# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a Rectangle object for the platform
platform = Rectangle(0, HEIGHT - 10, WIDTH, 10)




clock=pygame.time.Clock()
FPS = 100

# Main game loop
running = True
dragging = False

# COLORS = {"RED": (255, 0, 0), "BLUE": (0, 255, 0), "GREEN": (0, 0, 255), "WHITE" : (255, 255, 255), "BLACK" : (0,0,0)}
COLORS = {
    "RED": {"rgb": (255, 0, 0), "mass": 1.0, "density": 1.0},
    "BLUE": {"rgb": (0, 255, 0), "mass": 2.0, "density": 2.0},
    "GREEN": {"rgb": (0, 0, 255), "mass": 3.0, "density": 3.0},
    # "WHITE": {"rgb": (255, 255, 255), "mass": 0.0, "density": 0.0},
    # "BLACK": {"rgb": (0, 0, 0),  "mass": 0.0, "density": 0.0}
}


def create_object(ObjectType = "R", x=0, y=0, radius_x=0, radius_y=0, color="RED"):

    if ObjectType == "E":
        # This is the Ellipse case
        color = random.choice(list(COLORS))
        x = random.randint(0, WIDTH - radius_x)
        y = random.randint(0, HEIGHT - radius_y)
        radius_x = random.randint(10, 50)
        radius_y = random.randint(10, 50)
        Object = Ellipse(x, y, radius_x, radius_y, mass= COLORS[color]["mass"], density= COLORS[color]["density"], color= COLORS[color]["rgb"])
    elif ObjectType == "R":
        # This is the Rectangle case
        color = random.choice(list(COLORS))
        radius_x = random.randint(10, 50)
        radius_y = random.randint(10, 50)
        x = random.randint(0, WIDTH - radius_x)
        y = random.randint(0, HEIGHT - radius_y)
        Object = Rectangle(x, y, radius_x, radius_y, mass= COLORS[color]["mass"], density= COLORS[color]["density"], color= COLORS[color]["rgb"])

    return Object



def pygameStart():
    selected_obj = None  # No object is selected initially

    objects = [create_object("E")]

    running = True
    while running:
        # Fill the screen with white
        screen.fill((255, 255, 255))

        # Draw the platform
        pygame.draw.rect(screen, (0, 255, 0), (platform.x, platform.y, platform.width, platform.height))
        
        # print(objects[0].__class__.__name__)
        for i in objects:
            
                # print(i.color)
            if i.__class__.__name__ == "Rectangle":
                pygame.draw.rect(screen, i.color, (i.x, i.y, i.width, i.height))
            elif i.__class__.__name__ == "Ellipse":
                rect = pygame.Rect(i.x, i.y, i.width, i.height)
                pygame.draw.ellipse(screen, i.color, rect)

        for obj in objects:
            # Apply gravity to the object
            apply_acceleration(obj, 0, GRAVITY)

            if obj.y + obj.height > platform.y:

                apply_friction(obj, 1)

            # Simulate the object's motion
            simulate_rigid_body(obj)


            # BOUNCE
            if obj.y + obj.height > platform.y:
                obj.y = platform.y - obj.height 
                obj.velocity_y *= -COR
        


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
        if keys[pygame.K_w] and selected_obj:
            # apply_force(selected_obj, 0, -GRAVITY+10)
            selected_obj.velocity_y += 1
            # selected_obj.y -= 10  # Move up
        if keys[pygame.K_a] and selected_obj:
            selected_obj.velocity_x += 1
        if keys[pygame.K_s] and selected_obj:
            selected_obj.velocity_y -= 1
        if keys[pygame.K_d] and selected_obj:
            selected_obj.velocity_x += 1

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    

    pygameStart()


