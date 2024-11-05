#bensinbilkostnad#
a = 7500
b = 8.38*365
c = 1.0*10000
d = 0.3*10000

print("Bensinbil årlig kostnad =", a + b + c + d)

#elbilkostnad#

e = 5000
f = 8.38*365
g = 0.2*10000
h = (g*2.00)
i = 0.1*10000

print("El-bil årlig kostnad =", e + f + h + i)


import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Race")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Car settings
car_width = 50
car_height = 100
car_speed = 5

# Load car images
electric_car_img = pygame.image.load('output-onlinepngtools (1).png')
gasoline_car_img = pygame.image.load('output-onlinepngtools.png')

# Car positions
electric_car_x = 100
electric_car_y = screen_height - car_height - 10
gasoline_car_x = 600
gasoline_car_y = screen_height - car_height - 10

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move cars
    electric_car_y -= random.randint(1, car_speed)
    gasoline_car_y -= random.randint(1, car_speed)

    # Check for finish line
    if electric_car_y <= 0 or gasoline_car_y <= 0:
        running = False

    # Draw everything
    screen.fill(white)
    screen.blit(electric_car_img, (electric_car_x, electric_car_y))
    screen.blit(gasoline_car_img, (gasoline_car_x, gasoline_car_y))
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Determine winner
if electric_car_y <= 0 and gasoline_car_y <= 0:
    print("It's a tie!")
elif electric_car_y <= 0:
    print("Electric Car wins!")
else:
    print("Gasoline Car wins!")

# Quit Pygame
pygame.quit()
