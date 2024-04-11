import pygame
from physicsEngine import Rectangle, Ellipse, create_object , simulate_rigid_body,apply_acceleration, apply_friction
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

# 



def pygameStart():
    selected_obj = None  # No object is selected initially

    objects = [create_object("E"), create_object("R")]

    running = True
    while running:
        # Fill the screen with white
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

        for obj in objects:



            # Apply gravity to the object

            # shadow_polygon = draw_shadow(screen, obj) 

            # pygame.draw.polygon(screen, (0, 0, 0), shadow_polygon)

            apply_acceleration(obj, 0, GRAVITY)

            if obj.y + obj.height == platform.y  and obj.velocity_y < 0: 
                
                obj.acceleration_x -= obj.velocity_x * 0.1
                # simulate_rigid_body(obj)

            # Simulate the object's motion
            simulate_rigid_body(obj)

            # BOUNCE
            if obj.y + obj.height > platform.y:
                obj.y = platform.y - obj.height 
                obj.velocity_y *= -COR

            #Check for collision with walls
            # next_obj_x = obj.x + obj.velocity_x
            # next_obj_y = obj.y + obj.velocity_y
            # if ((obj.x < walls[0].x + walls[0].width and obj.x + obj.width > walls[0].x and obj.y < walls[0].y + walls[0].height and obj.y + obj.height > walls[0].y) or
            #     (next_obj_x < walls[0].x + walls[0].width and next_obj_x + obj.width > walls[0].x and next_obj_y < walls[0].y + walls[0].height and next_obj_y + obj.height > walls[0].y) or (obj.x < walls[1].x + walls[1].width and obj.x + obj.width > walls[1].x and obj.y < walls[1].y + walls[1].height and obj.y + obj.height > walls[1].y) or
            #     (next_obj_x < walls[1].x + walls[1].width and next_obj_x + obj.width > walls[1].x and next_obj_y < walls[1].y + walls[1].height and next_obj_y + obj.height > walls[1].y) ):
            #     if(obj.x < walls[0].x + walls[0].width and obj.x + obj.width > walls[0].x and obj.y < walls[0].y + walls[0].height and obj.y + obj.height > walls[0].y):
            #         obj.x = walls[0].x + walls[0].width
            #     elif(obj.x < walls[1].x + walls[1].width and obj.x + obj.width > walls[1].x and obj.y < walls[1].y + walls[1].height and obj.y + obj.height > walls[1].y):
            #         obj.x = walls[1].x - obj.width
            #     obj.velocity_x = -obj.velocity_x
            #     break
        
            if ((obj.x < walls[0].x + walls[0].width and obj.x + obj.width > walls[0].x and obj.y < walls[0].y + walls[0].height and obj.y + obj.height > walls[0].y) or
                (obj.x < walls[1].x + walls[1].width and obj.x + obj.width > walls[1].x and obj.y < walls[1].y + walls[1].height and obj.y + obj.height > walls[1].y)):
                if(obj.x < walls[0].x + walls[0].width and obj.x + obj.width > walls[0].x and obj.y < walls[0].y + walls[0].height and obj.y + obj.height > walls[0].y):
                    obj.x = walls[0].x + walls[0].width
                elif(obj.x < walls[1].x + walls[1].width and obj.x + obj.width > walls[1].x and obj.y < walls[1].y + walls[1].height and obj.y + obj.height > walls[1].y):
                    obj.x = walls[1].x - obj.width
                obj.velocity_x = -obj.velocity_x
                    # obj.y = platform.y - obj.height 
                    # obj.velocity_y = 0
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse is over an object
                mouse_pos = pygame.mouse.get_pos()
                for obj in objects:
                    if obj.x < mouse_pos[0] < obj.x + obj.width and obj.y < mouse_pos[1] < obj.y + obj.height:
                        selected_obj = obj
                        print(selected_obj.id)  # Select the object
                        break

        # Get the state of the keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and selected_obj:
            # apply_force(selected_obj, 0, -GRAVITY+10)
            selected_obj.velocity_y -= 1
            # selected_obj.y -= 10  # Move up
        if keys[pygame.K_a] and selected_obj:
            selected_obj.velocity_x -= 1
        if keys[pygame.K_s] and selected_obj:
            selected_obj.velocity_y += 1
        if keys[pygame.K_d] and selected_obj:
            selected_obj.velocity_x += 1

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    

    pygameStart()


