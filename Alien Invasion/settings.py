class Settings():
    """Class to store settings for the game"""
    
    def __init__(self):
        """Initialize game static settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) # set background color (blue like PowerShell)
        
        #Alien settings
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 3
        
        
        #Bullet settings
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        #Ship settings
        #self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        #How quicly the game speeds up
        self.speedup_scale = 1.1
        #How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change trough the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50
        
        #fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)