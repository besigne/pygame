import pygame


class Player(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = True
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

        self.char = pygame.image.load('imgs/standing.png')
        self.walkRight = [pygame.image.load('imgs/R1.png'),
                          pygame.image.load('imgs/R2.png'),
                          pygame.image.load('imgs/R3.png'),
                          pygame.image.load('imgs/R4.png'),
                          pygame.image.load('imgs/R5.png'),
                          pygame.image.load('imgs/R6.png'),
                          pygame.image.load('imgs/R7.png'),
                          pygame.image.load('imgs/R8.png'),
                          pygame.image.load('imgs/R9.png')]

        self.walkLeft = [pygame.image.load('imgs/L1.png'),
                         pygame.image.load('imgs/L2.png'),
                         pygame.image.load('imgs/L3.png'),
                         pygame.image.load('imgs/L4.png'),
                         pygame.image.load('imgs/L5.png'),
                         pygame.image.load('imgs/L6.png'),
                         pygame.image.load('imgs/L7.png'),
                         pygame.image.load('imgs/L8.png'),
                         pygame.image.load('imgs/L9.png')]

    def draw(self, win):

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            else:
                win.blit(self.walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def hit(self, win):
        self.x = 60
        self.y = 410
        self.walkCount = 0
        self.isJump = False
        self.jumpCount = 10
        font = pygame.font.SysFont('comicsans', 100)
        text = font.render('-5', True, (255, 0, 0))
        win.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 50:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 101
                    pygame.quit()
