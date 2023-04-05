import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    half_screen_height = SCREEN_HEIGHT // 2
    half_screen_width = SCREEN_WIDTH // 2
    def __init__(self, screen, message):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

    def update(self, game):
        self.handle_events(game)
        pygame.display.update()

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            if event.type == pygame.KEYDOWN:
                game.run()

    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

    def show_best_score(self, score):
        self.text = self.font.render(f"Best score: {score}", True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width + 200, self.half_screen_height + 50)

    def show_actual_score(self, score):
        self.text = self.font.render(f"Score: {score}", True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width - 200 , self.half_screen_height + 50)

    def show_death_count(self, count):
        self.text = self.font.render(f"Death count: {count}", True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height + 100)
                