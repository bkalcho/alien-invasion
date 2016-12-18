# Author: Bojan G. Kalicanin
# Date: 18-Dec-2016
# Game statistics

class GameStats(object):
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Starts Alien Invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the time."""
        self.ships_left = self.ai_settings.ship_limit