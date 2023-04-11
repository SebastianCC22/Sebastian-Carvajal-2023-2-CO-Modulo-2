import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.bird import Bird

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SHIELD_TYPE, DEFAULT_TYPE

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            self.select_obstacle = random.randint(0, 2)
            if self.select_obstacle == 0:
                self.obstacles.append(Bird(BIRD))
            elif self.select_obstacle  == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif self.select_obstacle == 2:
                self.obstacles.append(Cactus(SMALL_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE:
                    game.death_count.update()
                    game.power_up_manager.hammer = []
                    game.player.type = DEFAULT_TYPE
                    game.playing = False
                    break
                else:
                    self.reset_obstacles()

            if len(game.power_up_manager.hammer) == 1:
                if obstacle.rect.colliderect(game.power_up_manager.hammer[0].rect):
                    self.reset_obstacles()
                    game.power_up_manager.hammer = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []