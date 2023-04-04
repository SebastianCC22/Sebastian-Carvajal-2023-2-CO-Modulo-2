import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            self.cactus = [SMALL_CACTUS, LARGE_CACTUS]
            self.bird = [BIRD]
            self.select_obstacle = random.randint(0, 1)
            self.select_cactus = self.cactus[random.randint(0, 1)]

            if self.select_obstacle == 0:
                self.ramdon = self.cactus[random.randint(0, 1)]
                self.obstacles.append(Cactus(self.select_cactus))
            elif self.select_obstacle == 1:
                self.obstacles.append(Bird(self.bird[0]))
            # self.obstacles.append(Bird(self.bird[0]))
            # self.obstacles.append(Cactus(self.ramdon))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            if self.select_cactus == SMALL_CACTUS:
                obstacle.rect.y = 325
                obstacle.draw(screen)
            elif self.select_cactus == LARGE_CACTUS:
                obstacle.rect.y = 300
                obstacle.draw(screen)
            else:
                obstacle.rect.y = random.choice([100, 150, 200, 250, 300])
                obstacle.draw(screen)