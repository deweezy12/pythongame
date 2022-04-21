class GameStats:
	"""Track statistics for alien invasion"""

	def __init__(self, ai_game):
		"""initialize statistics"""
		self.settings = ai_game.settings
		self.reset_stats()

		#start alien invasion in an active state
		self.game_active = True

	def reset_stats(self):
		"""initialize statistics that can change during the game"""
		self.ships_left = self.settings.ship_limit