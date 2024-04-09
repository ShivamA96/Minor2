import pygame
from physicsEngineV3 import PyEn
WIDTH, HEIGHT = 1920, 600
GRAVITY = 9.8
COR = 0.5
FPS = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a Rectangle object for the platform
platform = PyEn("R",0, HEIGHT - 10, WIDTH, 10)
walls = [PyEn("R",0, 0, 10, HEIGHT), PyEn("R",WIDTH - 10, 0, 10, HEIGHT)]


clock=pygame.time.Clock()

# Main game loop
running = True
dragging = False

# font = pygame.font.Font(None, 24)





COLORS = {
    "RED": {"rgb": (255, 0, 0), "density": 0.01},
    "BLUE": {"rgb": (0, 255, 0),  "density": 0.02},
    "GREEN": {"rgb": (0, 0, 255),  "density": 0.03},
}



def pygameStart():
    selected_obj = None  # No object is selected initially

    objects = [PyEn("E",  100, 200, 50, 50,0.01, 1, color=(255, 0, 0) ), PyEn("R", 200, 300, 50, 50,0.01, 2, color=(0, 255, 0))]

    running = True


    while running:

        


        screen.fill((255, 255, 255))
        
        # Draw the platform
        pygame.draw.rect(screen, (0, 255, 0), (platform.x, platform.y, platform.width, platform.height))
        pygame.draw.rect(screen, (0, 255, 0), (walls[0].x, walls[0].y, walls[0].width, walls[0].height))
        pygame.draw.rect(screen, (0, 255, 0), (walls[1].x, walls[1].y, walls[1].width, walls[1].height))

        # make an inclined plane
        # pygame.draw.polygon(screen, (0, 255, 0), [(0, HEIGHT - 10), (WIDTH, HEIGHT - 10), (WIDTH, HEIGHT), (0, HEIGHT)])
        

        
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

        if keys[pygame.K_UP] and selected_obj:
            selected_obj.projectile_motion(2,45.0)
        if keys[pygame.K_w] and selected_obj:

            selected_obj.w_counter = 0.5
            # selected_obj.force_y = 0
            # selected_obj.simulate_rigid_body_by_player_y()
            # apply_force(selected_obj, 0, -GRAVITY+10)
            selected_obj.force_by_player_y(-selected_obj.w_counter)
            # selected_obj.a_counter = 0.0
            # selected_obj.s_counter = 0.0
            # selected_obj.d_counter = 0.0
            # selected_obj.y -= 10  # Move up
        elif keys[pygame.K_a] and selected_obj:
            selected_obj.a_counter = 5            
            # selected_obj.force_x = 0
            # selected_obj.simulate_rigid_body_by_player_x()
            selected_obj.force_by_player_x(-selected_obj.a_counter)

            # selected_obj.w_counter = 0
            # selected_obj.s_counter = 0
            # selected_obj.d_counter = 0

        elif keys[pygame.K_s] and selected_obj:
            selected_obj.s_counter = 0.5
            # selected_obj.force_y = 0
            # selected_obj.simulate_rigid_body_by_player_y()aaaaaa

            
            selected_obj.force_by_player_y(selected_obj.s_counter)

            # selected_obj.d_counter = 0
            # selected_obj.w_counter = 0
            # selected_obj.a_counter = 0

        elif keys[pygame.K_d] and selected_obj:
            selected_obj.d_counter = 5
            # selected_obj.force_x = 0
            # selected_obj.simulate_rigid_body_by_player_x()
            
            selected_obj.force_by_player_x(selected_obj.d_counter)
            
            # selected_obj.w_counter = 0
            # selected_obj.a_counter = 0
            # selected_obj.s_counter = 0


        # print(objects[0].__class__.__name__)
        for i in objects:
            
                # print(i.color)
            # Create a font object once and render the text onto a surface
            
            if i.type == "R":
                pygame.draw.rect(screen, i.color, (i.x, i.y, i.width, i.height))
                # force_surface = font.render(f"Force: ({float(i.force_x)}, {float(i.force_y)})", True, (0, 0, 0))
                # screen.blit(force_surface, (i.x, i.y))
            elif i.type == "E":
                rect = pygame.Rect(i.x, i.y, i.width, i.height)
                pygame.draw.ellipse(screen, i.color, rect)
                # force_surface = font.render(f"Force: ({float(i.force_x)}, {float(i.force_y)})", True, (0,0,0))
                # screen.blit(force_surface,(i.x, i.y))


        # for obj in objects:

        # PyEn.handle_collision(objects)

            
        

        for obj in objects:

            

            # APPLY GRAVITY
            obj.apply_acceleration_y(GRAVITY)


            # FRICTION

            if obj.y + obj.height > platform.y and obj.velocity_y > 0:

                # apply_acceleration(obj, -obj.velocity_x * 0.1, 0)
                obj.apply_friction(1)

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
                
                

                break
     



        for obj in objects:
            obj.simulate_rigid_body_x()
            obj.simulate_rigid_body_y()
        
        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":

    pygameStart()