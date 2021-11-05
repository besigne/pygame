import pygame
pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

walkRight = [pygame.image.load('imgs/R1.png'),
             pygame.image.load('imgs/R2.png'),
             pygame.image.load('imgs/R3.png'),
             pygame.image.load('imgs/R4.png'),
             pygame.image.load('imgs/R5.png'),
             pygame.image.load('imgs/R6.png'),
             pygame.image.load('imgs/R7.png'),
             pygame.image.load('imgs/R8.png'),
             pygame.image.load('imgs/R9.png')]

walkLeft = [pygame.image.load('imgs/L1.png'),
            pygame.image.load('imgs/L2.png'),
            pygame.image.load('imgs/L3.png'),
            pygame.image.load('imgs/L4.png'),
            pygame.image.load('imgs/L5.png'),
            pygame.image.load('imgs/L6.png'),
            pygame.image.load('imgs/L7.png'),
            pygame.image.load('imgs/L8.png'),
            pygame.image.load('imgs/L9.png')]

bg = pygame.image.load('imgs/bg.jpg')
char = pygame.image.load('imgs/standing.png')

screenWidth = 500
screenHeight = 500
x = 10
y = 400
width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10
left = False
Right = False
walkCount = 0


def redraw_game_window():
    global walkCount
    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))

    pygame.display.update()


run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        right = True
        left = False
    else:
        left = False
        right = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg * 0.5
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    redraw_game_window()

pygame.quit()
