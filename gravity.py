import pygame
from physicsEngine import Rectangle,Ellipse, apply_force, simulate_rigid_body,apply_acceleration

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
GRAVITY = 0.98

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







def create_object(Object):
    
    
    
    if Object=="Rectangle":

        
        color = random.choice(list(COLORS))
        
        height = random.randint(10, 50)
        width = random.randint(10, 50)


        x_cord = random.randint(0, WIDTH - width)
        y_cord = random.randint(0, HEIGHT - height)

        # print(x_cord, y_cord, width, height, color, COLORS[color]["mass"], COLORS[color]["density"])


        Object = Rectangle(x_cord, y_cord, width, height, mass= COLORS[color]["mass"], density= COLORS[color]["density"], color= COLORS[color]["rgb"])
        print(COLORS[color]["rgb"])

        return Object
    # if Object=="Ellipse":

    #     width = random.randint(10, 50)
    #     height = random.randint(10, 50)
        
    #     x_cord = random.randint(0, WIDTH - width)
    #     y_cord = random.randint(0, HEIGHT - height)

    #     color = random.choice(list(COLORS.values()))

    #     Object = Ellipse(x_cord, y_cord, width, height, mass= color["mass"], density= color["density"])

    #     Rect = pygame.Rect(x_cord, y_cord, Object.radius, height)

    #     pygame.draw.ellipse(screen, (0, 0, 255),  )


# def create_object(Object):
    
    
    
#     if Object=="Rectangle":

        
#         color = random.choice(list(COLORS))
        
#         height = random.randint(10, 50)
#         width = random.randint(10, 50)


#         x_cord = random.randint(0, WIDTH - width)
#         y_cord = random.randint(0, HEIGHT - height)

#         print(COLORS[color]["rgb"])

#         Object = Rectangle(x_cord, y_cord, width, height, mass= COLORS[color]["mass"], density= COLORS[color]["density"], color= COLORS[color]["rgb"])

#         return Object
    # if Object=="Ellipse":

    #     width = random.randint(10, 50)
    #     height = random.randint(10, 50)
        
    #     x_cord = random.randint(0, WIDTH - width)
    #     y_cord = random.randint(0, HEIGHT - height)

    #     color = random.choice(list(COLORS.values()))

    #     Object = Ellipse(x_cord, y_cord, width, height, mass= color["mass"], density= color["density"])

    #     Rect = pygame.Rect(x_cord, y_cord, Object.radius, height)

    #     pygame.draw.ellipse(screen, (0, 0, 255),  )


def pygameStart():
    selected_obj = None  # No object is selected initially

    objects = [create_object("Ellipse")]

    print(objects[0].color)


    running = True
    while running:
        # Fill the screen with white
        screen.fill((255, 255, 255))

        # Draw the platform
        pygame.draw.rect(screen, (0, 255, 0), (platform.x, platform.y, platform.width, platform.height))

        for i in objects:
            # print(i.color)
            pygame.draw.rect(screen, i.color, (i.x, i.y, i.width, i.height))

        for obj in objects:
            # Apply gravity to the object
            apply_acceleration(obj, 0, GRAVITY)

            # Simulate the object's motion
            simulate_rigid_body(obj)

            # Stop the object when it hits the platform
            if obj.y + obj.height > platform.y:
                obj.y = platform.y - obj.height
                obj.velocity_y = 0

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
            apply_acceleration(selected_obj, 0, -GRAVITY)
            simulate_rigid_body(selected_obj)
            # selected_obj.y -= 10  # Move up
        if keys[pygame.K_a] and selected_obj:
            selected_obj.x -= 5  # Move left
        if keys[pygame.K_s] and selected_obj:
            selected_obj.y += 5  # Move down
        if keys[pygame.K_d] and selected_obj:
            selected_obj.x += 5  # Move right

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    

    pygameStart()


