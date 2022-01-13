from config.config import *

class Bullet(arcade.Sprite):
    
    def __init__(self, host): 
        super().__init__(':resources:images/space_shooter/laserRed01.png',SPRITE_SCALING_LASER)
        self.speed = BULLET_SPEED
        self.angle = host.angle
        self.center_x = host.center_x
        self.center_y = host.center_y

   

    def update(self):
        angle_radious = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_radious)
        self.center_y += self.speed * math.cos(angle_radious)
