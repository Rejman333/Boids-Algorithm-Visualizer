import pygame

SLIDER_COLOR = (120, 120, 180)
SLIDER_HIGH = 4
SLIDER_WIDTH = 200
SLIDER_BORDER_RADIUS = 10

SLIDER_VALUE_INDICATOR_COLOR = (190, 85, 85)
SLIDER_INDICATOR_SIZE = 5


class Slider:
    def __init__(self, name, slider_font, slider_position_x, slider_position_y, min_value, max_value, scale,
                 base_value=None):
        self.name = name

        self.slider_font = slider_font

        self.min_value = min_value
        self.max_value = max_value
        self.scale = scale
        self.value = base_value if base_value else (max_value+min_value) / 2

        self.position_x = slider_position_x
        self.position_y = slider_position_y

        self.slider_rect = pygame.Rect(self.position_x, self.position_y, SLIDER_WIDTH, SLIDER_HIGH)
        self.slider_indicator_position = self.slider_rect.center

    def draw(self, display_surf):
        text = f"{self.name}: {self.value}"
        text_surface = self.slider_font.render(text, False, SLIDER_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.midbottom = self.slider_rect.midtop
        display_surf.blit(text_surface, text_rect)
        pygame.draw.rect(display_surf, SLIDER_COLOR, self.slider_rect, border_radius=SLIDER_BORDER_RADIUS)
        pygame.draw.circle(display_surf, SLIDER_VALUE_INDICATOR_COLOR, self.slider_indicator_position,
                           SLIDER_INDICATOR_SIZE)

    def is_mouse_touching(self, mouse_position):
        mouse_position_x, mouse_position_y = mouse_position
        slider_indicator_position_x, slider_indicator_position_y = self.slider_indicator_position

        if (abs(mouse_position_x - slider_indicator_position_x) <= SLIDER_INDICATOR_SIZE and
                abs(mouse_position_y - slider_indicator_position_y) <= SLIDER_INDICATOR_SIZE):
            return True

        if self.slider_rect.collidepoint(mouse_position_x, mouse_position_y):
            return True

    def move_indicator(self, mouse_position):
        new_x, _ = mouse_position
        _, old_y = self.slider_indicator_position

        if new_x < self.position_x:
            new_x = self.position_x
        elif new_x > self.position_x + SLIDER_WIDTH:
            new_x = self.position_x + SLIDER_WIDTH

        self.slider_indicator_position = (new_x, old_y)
        new_value = round(((new_x - self.slider_rect.x) / SLIDER_WIDTH ) * (self.max_value - self.min_value) + self.min_value, 3)
        self.value = new_value
