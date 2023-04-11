from dino_runner.utils.constants import HAMMER_TYPE, HAMMER

from dino_runner.components.power_ups.power_up import PowerUp

class Hammer(PowerUp):
    def __init__(self):
        self.hammer_launched = False
        super().__init__(HAMMER, HAMMER_TYPE)

    def update_hammer_launched(self, game_speed):
        self.rect.x += game_speed