import pygame
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, DEFAULT_TYPE,HAMMER


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3, 5)
        self.appear_when = random.randint(50, 70)

    def update(self, game, user_input):
        if len(self.power_ups) == 0 and self.appear_when == game.score.count:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if power_up.type == SHIELD_TYPE:
                if game.player.dino_rect.colliderect(power_up.rect):
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.has_power_up = True
                    game.player.type = SHIELD_TYPE
                    game.player.power_up_time = power_up.start_time + \
                        (self.duration * 1000)

                    self.power_ups.remove(power_up)
            # elif power_up.type == HAMMER_TYPE:
            #     if game.player.dino_rect.colliderect(power_up.rect):
            #         power_up.start_time = pygame.time.get_ticks()
            #         game.player.has_power_up = True
            #         game.player.type = power_up.type
            #         if game.player.type == HAMMER_TYPE:
            #             self.hammer.append(Hammer())
            #         game.player.power_up_time = power_up.start_time + \
            #             (self.duration * 1000)

            #         self.power_ups.remove(power_up)
            
            # if game.player.type == HAMMER_TYPE and user_input[pygame.K_SPACE]:
            #     game.player.type = DEFAULT_TYPE
            #     self.hammer[0].hammer_launched = True
            #     self.hammer[0].rect.x = game.player.X_POS
            #     self.hammer[0].rect.y = game.player.dino_rect.y

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)


        if len(self.hammer) == 1:
            if self.hammer[0].hammer_launched:
                self.hammer[0].draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.hammer = []
        self.appear_when = random.randint(50, 70)

    def generate_power_up(self):
        self.appear_when += random.randint(200, 300)
        power_up = Shield()
        # power_up = random.choice([Shield(), Hammer()])
        self.power_ups.append(power_up)

