import pygame
import sys
import random
pygame.init()
class flappy():

    def __init__(self):
        self.b = pygame.display.set_mode((400, 708))
        self.a = (pygame.image.load("0.png").convert_alpha(),pygame.image.load("1.png").convert_alpha(),
                  pygame.image.load("2.png").convert_alpha(),
                  pygame.image.load("dead.png").convert_alpha()
                    )
        self.background = pygame.image.load("background.png").convert()
        self.pipe1 = pygame.image.load("bottom.png").convert()
        self.pipe2 = pygame.image.load("top.png").convert()
        self.sound = pygame.mixer.Sound("sound1.wav")
        self.bird = pygame.Rect(70, 50, 40, 30)
        self.birdY = 0
        self.gravity = .1
        self.sprite = 0
        self.speed = .01
        self.gap = 150
        self.offset = random.randint(-160, 160)
        self.pipex = 400
        self.birdydead = False
        self.counter = 0

    def pipeupdate(self):
        self.pipex = self.pipex - 2.2
        if self.pipex < -150:
            self.pipex = 400
            self.offset = random.randint(-160, 160)
            self.counter = self.counter + 1
    def birdupdate(self):
        if 2.5 < self.speed < 3.5:
            self.sprite = 2
        if 1 < self.speed < 1.5:
            self.sprite = 1

        if not 0 < self.birdY < 720:
            self.birdydead = False
            self.birdY = 2
            self.speed = .1
            self.pipex = 450
            self.gravity = .1
            self.counter = 0
        self.bird[1] = self.birdY
        pipe1rect = pygame.Rect(self.pipex, 360 + self.gap - self.offset,self.pipe1.get_width()
                                , self.pipe1.get_height())
        pipe2rect = pygame.Rect(self.pipex, 0 - self.gap - self.offset, self.pipe1.get_width()
                                , self.pipe1.get_height())

        if pipe1rect.colliderect(self.bird):
            self.birdydead = True

        if pipe2rect.colliderect(self.bird):
            self.birdydead = True

        self.birdY = self.birdY - self.speed
        self.speed = self.speed - self.gravity
        self.gravity = self.gravity + .004


    def jump(self):
        self.speed = 4


    def run(self):
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("Impact", 40)
        while True:
            clock.tick(60)
            for c in pygame.event.get():
                if c.type == pygame.QUIT:
                    sys.exit()
                if (c.type == pygame.KEYDOWN or c.type == pygame.MOUSEBUTTONDOWN) and self.birdydead == False:
                    self.sound.play()
                    self.gravity = .1
                    self.jump()
            if self.birdydead == True:
                self.sprite = 3
            else:
                self.sprite = 0
            self.pipeupdate()
            self.birdupdate()

            self.b.fill((255, 255, 255))
            self.b.blit(self.background, (0, 0))
            self.b.blit(self.a[self.sprite],(70,self.birdY))
            self.b.blit(self.pipe1 , (self.pipex,350 + self.gap - self.offset))
            self.b.blit(self.pipe2, (self.pipex, 0 - self.gap - self.offset))
            self.b.blit(font.render(str(self.counter),
                                    10,
                                    (255, 255, 255)),
                        (200, 50))

            pygame.display.update()


if __name__ == "__main__":
    flappy().run()
