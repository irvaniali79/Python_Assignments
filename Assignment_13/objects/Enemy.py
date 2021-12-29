import random
from config.config import *

class Enemy(arcade.Sprite):
    
    def __init__(self):
        super().__init__(':resources:images/space_shooter/playerShip1_green.png',SPRITE_SCALING_ENEMY)
        self.speed = SHIP_SPEED
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = SCREEN_HEIGHT+10  
        self.angle = 180
        self.width = 50
        self.height = 50

    def hit(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/hit3.wav'), 1.0, 0.0,False)

    def update(self):
        self.center_y -= self.speed  
