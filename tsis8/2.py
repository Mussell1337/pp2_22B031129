import pygame
import random

# set up game window
pygame.init()
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# load images
car_img = pygame.image.load("img/car.png")
coin_img = pygame.image.load("img/coin.png")
road_img = pygame.image.load("img/road.png")

# set up variables
car_x = WIDTH // 2 - car_img.get_width() // 2
car_y = HEIGHT - car_img.get_height() - 10
coin_list = []
coin_count = 0
car_speed = 1 # adjust car speed here
coin_speed = 1 # adjust coin speed here

# game loop
run = True
while run:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update game state
    # move car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    elif keys[pygame.K_RIGHT] and car_x < WIDTH - car_img.get_width():
        car_x += car_speed

    # add coins randomly
    if len(coin_list) < 5 and random.random() < 0.05:
        coin_x = random.randint(0, WIDTH - coin_img.get_width())
        coin_y = -coin_img.get_height()
        coin_list.append((coin_x, coin_y))

    # update coin positions and remove coins that go off screen
    for i, (coin_x, coin_y) in enumerate(coin_list):
        coin_y += coin_speed
        if coin_y > HEIGHT:
            del coin_list[i]
            continue
        coin_list[i] = (coin_x, coin_y)

        # check for collision with car
        if car_x < coin_x + coin_img.get_width() and car_x + car_img.get_width() > coin_x \
                and car_y < coin_y + coin_img.get_height() and car_y + car_img.get_height() > coin_y:
            coin_count += 1
            del coin_list[i]

    # draw everything
    win.blit(road_img, (0, 0))
    for coin_x, coin_y in coin_list:
        win.blit(coin_img, (coin_x, coin_y))
    win.blit(car_img, (car_x, car_y))
    font = pygame.font.Font(None, 36)
    text = font.render(f"Coins: {coin_count}", True, (255, 255, 255))
    win.blit(text, (WIDTH - text.get_width() - 10, 10))

    pygame.display.update()

# quit game
pygame.quit()