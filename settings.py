class Settings:
	"""A class to store all settings for Alien Ivasion."""

	def __init__(self):
		"""Initialize the games settings"""
		#Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		#ship settings
		self.ship_speed = 1.2
		self.ship_limit = 3

		#bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		#alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 50
		#fleet_diretion of 1 respresents right, -1 represents left
		self.fleet_direction = 1