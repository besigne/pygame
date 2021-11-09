import pygame
from classes.char import Player
from classes.enemy import Enemy
from classes.projectile import Projectile

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")

clock = pygame.time.Clock()
bg = pygame.image.load('imgs/bg.jpg')

screenWidth = 500
screenHeight = 480


def redraw_game_window():
    win.blit(bg, (0, 0))
    man.draw(win)
    goblin.draw(win)
    for redraw_bullet in bullets:
        redraw_bullet.draw(win)
    pygame.display.update()


run = True
man = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []

while run:
    clock.tick(27)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3]\
                and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0]\
                    and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))

        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(x=round(man.x + man.width // 2),
                                      y=round(man.y + man.height // 2),
                                      radius=6,
                                      color=(0, 0, 0),
                                      facing=facing))
        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.standing = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg * 0.5
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    redraw_game_window()

pygame.quit()
