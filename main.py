import pygame
import math
import random

pygame.init()

class Target:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def move(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 100, 100), (self.x, self.y), self.radius)

class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x += 0.4

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 200, 100), (self.x, self.y), 10)

    def detectCollisionTarget(self, target):
        distance = math.sqrt((self.y - target.y)**2 + (self.x - target.x)**2)
        if distance < 10 + target.radius:
            return True
        return False

class Player:
    def __init__(self):
        self.x = 100
        self.y = 250
        self.dy = 0
        self.dx = 0

    def move(self):
        self.y += self.dy
        if self.y < 0:
            self.y -= self.dy

        if self.y > 500:
            self.y -= self.dy

        self.x += self.dx
        if self.x < 0:
            self.x -= self.dx

        if self.x > 1000:
            self.x -= self.dx

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 255), pygame.Rect(self.x-15, self.y-15, 30, 30))


def main():
    screen = pygame.display.set_mode((1000, 500))
    playerShip = Player()

    projectiles = []
    targets = [Target(random.randint(500, 1000), random.randint(0, 500), random.randint(20, 50))]

    gameOver = False

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameOver = True

                if event.key == pygame.K_w:
                    playerShip.dy = -0.2

                if event.key == pygame.K_s:
                    playerShip.dy = 0.2

                if event.key == pygame.K_a:
                    playerShip.dx = -0.2

                if event.key == pygame.K_d:
                    playerShip.dx = 0.2


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    playerShip.dy = 0
                if event.key == pygame.K_s:
                    playerShip.dy = 0

                if event.key == pygame.K_a:
                    playerShip.dx = 0
                if event.key == pygame.K_d:
                    playerShip.dx = 0

                if event.key == pygame.K_SPACE:
                    projectiles.append(Projectile(playerShip.x, playerShip.y))

        screen.fill((0, 0, 0))
        playerShip.move()
        playerShip.draw(screen)
        for object in projectiles:
            object.move()
            object.draw(screen)
            for target in targets:
                if object.detectCollisionTarget(target):
                    targets.remove(target)
                    projectiles.remove(object)
                    targets.append(Target(random.randint(500, 1000), random.randint(0, 500), random.randint(20, 50)))
        for target in targets:
            target.draw(screen)
        pygame.display.update()

main()
