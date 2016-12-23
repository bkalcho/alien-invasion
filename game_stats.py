# Author: Bojan G. Kalicanin
# Date: 18-Dec-2016
# Game statistics

import os

class GameStats(object):
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings, highscore_file):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start game in an inactive state.
        self.game_active = False
        
        # High score should never be reset.
        self.highscore_file = highscore_file
        if os.path.exists(self.highscore_file):
            f_obj = open(highscore_file, 'r')
            content = f_obj.read()
            if len(content) > 0:
                self.high_score = int(content.rstrip())
            else:
                self.high_score = 0
        else:
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the time."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1