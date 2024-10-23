import random
import math
from pygame import draw


class Particle:
    def __init__(self, display_surf_width, display_surf_height):
        self.x = random.random() * display_surf_width
        self.y = random.random() * display_surf_height
        self.velocity_x = random.random() * 6 - 3
        self.velocity_y = random.random() * 6 - 3

    def draw(self, display_surf, color, particle_size):
        draw.circle(display_surf, color, (self.x, self.y), particle_size)
        draw.line(display_surf, (200, 200, 200), (self.x, self.y), (self.velocity_x + self.x, self.velocity_y + self.y))

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def avoid_walls(self, walls_margin, walls_turn_factor, display_surf_width, display_surf_height):
        if self.x < walls_margin:
            self.velocity_x += walls_turn_factor

        if self.x > display_surf_width - walls_margin:
            self.velocity_x -= walls_turn_factor

        if self.y < walls_margin:
            self.velocity_y += walls_turn_factor

        if self.y > display_surf_height - walls_margin:
            self.velocity_y -= walls_turn_factor

    def move_to_center(self, particle_list, visual_range, centering_factor):
        center_x = 0
        center_y = 0
        number_of_visible_particles = 0

        for particle in particle_list:
            if particle_distance(self, particle) < visual_range:
                center_x += particle.x
                center_y += particle.y
                number_of_visible_particles += 1

        if number_of_visible_particles:
            center_x = center_x / number_of_visible_particles
            center_y = center_y / number_of_visible_particles

            self.velocity_x += (center_x - self.x) * centering_factor
            self.velocity_y += (center_y - self.y) * centering_factor

    def separate(self, particle_list, min_distance, avoidance_factor):
        move_x = 0
        move_y = 0

        for particle in particle_list:
            if particle != self:
                if particle_distance(self, particle) < min_distance:
                    move_x = self.x - particle.x
                    move_y = self.y - particle.y

        self.velocity_x += move_x * avoidance_factor
        self.velocity_y += move_y * avoidance_factor

    def obey_spead_limit(self, speed_limit):
        spead = math.sqrt(self.velocity_x ** 2 + self.velocity_y ** 2)

        if spead > speed_limit:
            self.velocity_x = (self.velocity_x / spead) * speed_limit
            self.velocity_y = (self.velocity_y / spead) * speed_limit

    def match_velocity(self, particle_list, visual_range, matching_factor):
        sum_velocity_x = 0
        sum_velocity_y = 0
        number_of_visible_particles = 0

        for particle in particle_list:
            if particle_distance(self, particle) < visual_range:
                sum_velocity_x += particle.velocity_x
                sum_velocity_y += particle.velocity_y
                number_of_visible_particles += 1

        if number_of_visible_particles:
            average_velocity_x = sum_velocity_x / number_of_visible_particles
            average_velocity_y = sum_velocity_y / number_of_visible_particles

            self.velocity_x += (average_velocity_x - self.velocity_x) * matching_factor
            self.velocity_y += (average_velocity_y - self.velocity_y) * matching_factor


def particle_distance(particle_1, particle_2):
    return math.sqrt((particle_1.x - particle_2.x) ** 2 * (particle_1.y - particle_2.y) ** 2)
