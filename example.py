import pygame
import math

pygame.init()

WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()

# Game variables
wall_thickness = 10
gravity = 0.5
bounce_stop = 0.3

# Track positions of mouse to get movement vector
mouse_trajectory = []


class Ball:
    def __init__(self, x_pos, y_pos, radius, color, mass, retention, y_speed, x_speed, id, friction):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.id = id
        self.circle = ''
        self.selected = False
        self.friction = friction

    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def check_gravity(self):
        if not self.selected:
            if self.y_pos < HEIGHT - self.radius - (wall_thickness / 2):
                self.y_speed += gravity
            else:   
                if self.y_speed > bounce_stop:
                    self.y_speed = self.y_speed * -1 * self.retention
                else:
                    if abs(self.y_speed) <= bounce_stop:
                        self.y_speed = 0
            if (self.x_pos < self.radius + (wall_thickness / 2) and self.x_speed < 0) or \
                    (self.x_pos > WIDTH - self.radius - (wall_thickness / 2) and self.x_speed > 0):
                self.x_speed *= -1 * self.retention
                if abs(self.x_speed) < bounce_stop:
                    self.x_speed = 0
            if self.y_speed == 0 and self.x_speed != 0:
                if self.x_speed > 0:
                    self.x_speed -= self.friction
                elif self.x_speed < 0:
                    self.x_speed += self.friction
        else:
            self.x_speed = x_push
            self.y_speed = y_push
        return self.y_speed

    def update_pos(self, mouse):
        if not self.selected:
            self.y_pos += self.y_speed
            self.x_pos += self.x_speed
        else:
            self.x_pos = mouse[0]
            self.y_pos = mouse[1]

    def check_select(self, pos):
        self.selected = False
        if self.circle.collidepoint(pos):
            self.selected = True
        return self.selected


def draw_walls():
    left = pygame.draw.line(screen, 'white', (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'white', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'white', (0, 0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'white', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list


def calc_motion_vector():
    x_speed = 0
    y_speed = 0
    if len(mouse_trajectory) > 10:
        x_speed = (mouse_trajectory[-1][0] - mouse_trajectory[0][0]) / len(mouse_trajectory)
        y_speed = (mouse_trajectory[-1][1] - mouse_trajectory[0][1]) / len(mouse_trajectory)
    return x_speed, y_speed


def check_collision(ball1, ball2):
    distance = math.sqrt((ball1.x_pos - ball2.x_pos) ** 2 + (ball1.y_pos - ball2.y_pos) ** 2)
    if distance <= ball1.radius + ball2.radius:
        return True
    return False


def handle_collision(ball1, ball2):
    # Calculate collision normal
    normal_x = ball2.x_pos - ball1.x_pos
    normal_y = ball2.y_pos - ball1.y_pos
    distance = math.sqrt(normal_x ** 2 + normal_y ** 2)
    normal_x /= distance
    normal_y /= distance

    # Calculate relative velocity
    relative_velocity_x = ball2.x_speed - ball1.x_speed
    relative_velocity_y = ball2.y_speed - ball1.y_speed

    # Calculate impulse
    impulse = (2.0 * (normal_x * relative_velocity_x + normal_y * relative_velocity_y)) / \
              (ball1.mass + ball2.mass)

    # Update velocities
    ball1.x_speed += impulse * ball2.mass * normal_x
    ball1.y_speed += impulse * ball2.mass * normal_y
    ball2.x_speed -= impulse * ball1.mass * normal_x
    ball2.y_speed -= impulse * ball1.mass * normal_y


# Font initialization
font = pygame.font.SysFont(None, 22)

# Ball initialization
ball1 = Ball(50, 50, 30, 'blue', 100, .75, 0, 0, 1, 0.02)
ball2 = Ball(500, 50, 70, 'green', 300, .9, 0, 0, 2, 0.03)
ball3 = Ball(200, 50, 50, 'purple', 200, .8, 0, 0, 3, 0.04)
ball4 = Ball(700, 50, 60, 'red', 500, .7, 0, 0, 4, .1)
balls = [ball1, ball2, ball3, ball4]

# Main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    mouse_coords = pygame.mouse.get_pos()
    mouse_trajectory.append(mouse_coords)
    if len(mouse_trajectory) > 20:
        mouse_trajectory.pop(0)
    x_push, y_push = calc_motion_vector()

    walls = draw_walls()
    ball1.draw()
    ball2.draw()
    ball3.draw()
    ball4.draw()
    ball1.update_pos(mouse_coords)
    ball2.update_pos(mouse_coords)
    ball3.update_pos(mouse_coords)
    ball4.update_pos(mouse_coords)
    ball1.y_speed = ball1.check_gravity()
    ball2.y_speed = ball2.check_gravity()
    ball3.y_speed = ball3.check_gravity()
    ball4.y_speed = ball4.check_gravity()

    # Displaying object attributes
    for ball in balls:
        text = font.render(f'x_speed: {ball.x_speed:.2f}, y_speed: {ball.y_speed:.2f}', True, (255, 255, 255))
        screen.blit(text, (ball.x_pos , ball.y_pos ))

    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if check_collision(balls[i], balls[j]):
                handle_collision(balls[i], balls[j])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if ball1.check_select(event.pos) or ball2.check_select(event.pos) \
                        or ball3.check_select(event.pos) or ball4.check_select(event.pos):
                    active_select = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_select = False
                for i in range(len(balls)):
                    balls[i].check_select((-1000, -1000))

    pygame.display.flip()

pygame.quit()
