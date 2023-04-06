from dino_runner.utils.constants import SHIELD_TYPE, SHIELD

from dino_runner.components.power_ups.power_up import PowerUp

class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)