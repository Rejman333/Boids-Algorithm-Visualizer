import pygame
from particle import Particle
from slider import Slider, SLIDER_WIDTH

BACKGROUND_COLOR = (20, 20, 20)
BLUE = (100, 100, 255)
LIGHT_BLUE = (0, 0, 255)
BLACK = (250, 250, 250)
GREEN = (80, 200, 40)
READ = (200, 80, 40)


class App:
    def __init__(self):
        self._running = False
        self._display_surf = None
        self.clock = None
        self.width = 1600
        self.height = 900
        self.font = None
        self.slider_font = None

        self.particle_limit = 125
        self.particle_size = 3
        self.particle_speed_limit = 15
        self.particle_list = None

        self.walls_margin = 50
        self.walls_turn_factor = 1

        self.visual_range = 50
        self.centering_factor = 0.005

        self.min_particle_distance = 10
        self.avoidance_factor = 0.05

        self.sliders_info = [("Coherence", 0, 0.02), ("Separation", 0, 0.05), ("Alignment", 0, 0.2), ("Speed Limit", 0, 10), ("Visual Range", 0, 250)]
        self.sliders_height = 875
        self.sliders_starting_width = 100
        self.sliders_margin = 100
        self.sliders_list = []

        self.index_of_interacted_slider = None

        self.matching_factor = 0.05

    def _draw_sliders(self):
        for slider in self.sliders_list:
            slider.draw(self._display_surf)

    def _draw_fps(self):
        text_surface = self.font.render("{:.2f}".format(self.clock.get_fps()), False, BLUE)
        self._display_surf.blit(text_surface, (0, 0))

    def _draw_particles(self):
        for particle in self.particle_list:
            particle.draw(self._display_surf, BLUE, self.particle_size)

    def _draw_walls(self):
        pygame.draw.rect(self._display_surf, GREEN,
                         pygame.Rect(self.walls_margin, self.walls_margin, self.width - self.walls_margin * 2,
                                     self.height - self.walls_margin * 2), 2)

    def _draw_special_particle(self):
        pygame.draw.circle(self._display_surf, READ, (self.particle_list[0].x, self.particle_list[0].y),
                           self.particle_size)
        pygame.draw.circle(self._display_surf, BLACK, (self.particle_list[0].x, self.particle_list[0].y),
                           self.visual_range, 1)
        pygame.draw.circle(self._display_surf, BLACK, (self.particle_list[0].x, self.particle_list[0].y),
                           self.min_particle_distance, 1)

    def on_init(self):
        pygame.init()
        # self._display_surf = pygame.display.set_mode((1920, 1080), pygame.OPENGL)

        self._display_surf = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.slider_font = pygame.font.SysFont('Comic Sans MS', 20)

        self.particle_list = [Particle(self.width, self.height) for _ in range(self.particle_limit)]
        for i, slider_info in enumerate(self.sliders_info):
            slider_name, min_val, max_val = slider_info
            slider = Slider(slider_name, self.slider_font, self.sliders_margin * (i + 1) + SLIDER_WIDTH * i,
                            self.sliders_height, min_val, max_val, 10)
            self.sliders_list.append(slider)

        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            for slider_index, slider in enumerate(self.sliders_list):
                if slider.is_mouse_touching(mouse_position):
                    self.index_of_interacted_slider = slider_index
                    slider.move_indicator(mouse_position)

        elif event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            if self.index_of_interacted_slider is not None:
                slider = self.sliders_list[self.index_of_interacted_slider]
                slider.move_indicator(mouse_position)

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.index_of_interacted_slider is not None:
                self.index_of_interacted_slider = None

    def on_loop(self):
        self.centering_factor = self.sliders_list[0].value
        self.avoidance_factor = self.sliders_list[1].value
        self.matching_factor = self.sliders_list[2].value
        self.particle_speed_limit = self.sliders_list[3].value
        self.visual_range = self.sliders_list[4].value

        for particle in self.particle_list:
            particle.move_to_center(self.particle_list, self.visual_range, self.centering_factor)
            particle.separate(self.particle_list, self.min_particle_distance, self.avoidance_factor)
            particle.match_velocity(self.particle_list, self.visual_range, self.matching_factor)
            particle.obey_spead_limit(self.particle_speed_limit)
            particle.avoid_walls(self.walls_margin, self.walls_turn_factor, self.width, self.height)
            particle.move()

    def on_render(self):
        self._display_surf.fill(BACKGROUND_COLOR)
        self._draw_walls()
        self._draw_particles()
        self._draw_special_particle()
        self._draw_fps()
        self._draw_sliders()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()
        while self._running:
            self.clock.tick(60)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
