import pygame
from physicsEngineV2 import Rectangle,Ellipse,simulate_rigid_body_for_screen, simulate_rigid_body,apply_acceleration, apply_friction, apply_force, force_by_player, create_object,handle_collision
from physicsEngineV2 import COLORS as COLORS

WIDTH, HEIGHT = 800, 600
GRAVITY = 0.98
COR = 0.5
FPS = 100

pygame.init()
import turtle
# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a Rectangle object for the platform
platform = Rectangle(0, HEIGHT - 10, WIDTH, 10)
walls = [Rectangle(0, 0, 10, HEIGHT), Rectangle(WIDTH - 10, 0, 10, HEIGHT)]


clock=pygame.time.Clock()

# Main game loop
running = True
dragging = False

font = pygame.font.Font(None, 24)

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

        # make an inclined plane
        pygame.draw.polygon(screen, (0, 255, 0), [(0, HEIGHT - 10), (WIDTH, HEIGHT - 10), (WIDTH, HEIGHT), (0, HEIGHT)])

        # print(objects[0].__class__.__name__)
        for i in objects:
            
                # print(i.color)
            # Create a font object once and render the text onto a surface
            
            if i.__class__.__name__ == "Rectangle":
                pygame.draw.rect(screen, i.color, (i.x, i.y, i.width, i.height))
                # force_surface = font.render(f"Force: ({float(i.force_x)}, {float(i.force_y)})", True, (0, 0, 0))
                # screen.blit(force_surface, (i.x, i.y))
            elif i.__class__.__name__ == "Ellipse":
                rect = pygame.Rect(i.x, i.y, i.width, i.height)
                pygame.draw.ellipse(screen, i.color, rect)
                # force_surface = font.render(f"Force: ({float(i.force_x)}, {float(i.force_y)})", True, (0,0,0))
                # screen.blit(force_surface,(i.x, i.y))


        # for obj in objects:

        # handle_collision(objects)

            
        

        for obj in objects:

            

            # APPLY GRAVITY
            apply_acceleration(obj, 0, GRAVITY)


            # FRICTION

            if obj.y + obj.height > platform.y and obj.velocity_y > 0:

                # apply_acceleration(obj, -obj.velocity_x * 0.1, 0)
                apply_friction(obj, 1)

            # BOUNCE
            if obj.y + obj.height > platform.y:
                obj.y = platform.y - obj.height 
                obj.velocity_y *= -COR
                # obj.force_y = -obj.force_y
                # simulate_rigid_body_for_screen(obj)
 

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
            selected_obj.a_counter += 0.5            
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
            selected_obj.d_counter += 0.5
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