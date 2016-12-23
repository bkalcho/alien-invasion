# Author: Bojan G. Kalicanin
# Date: 09-Dec-2016
# Main Game program

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Highscore file location.
    highscore_file = 'data\highscore.txt'

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings, highscore_file)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Start the main loop for the game.
    while True:
        gf.check_events(highscore_file, ai_settings, screen, stats, sb,
            play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                    bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens,
                    bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
            play_button)

run_game()
