from config.config import *
from objects.Bullet import Bullet

class Spacecraft(arcade.Sprite):
    
    def __init__(self):

        super().__init__(':resources:images/space_shooter/playerShip3_orange.png',SPRITE_SCALING_PLAYER)
        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser2.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/explosion2.wav")
       
        self.width = 48
        self.height = 48
        
        self.center_x = SCREEN_WIDTH//2
        self.center_y = 50

        self.change_x = 0
        self.change_y = 0

        self.angle = 0
        self.change_angle = 0

        self.bullet_list =arcade.SpriteList()
        self.HP = "assets/heart.png"
        self.HPs = [arcade.Sprite(self.HP, 0.1 , center_x=30 , center_y=50) , arcade.Sprite(self.HP, 0.1 , center_x=80 , center_y=50) ,arcade.Sprite(self.HP, 0.1 ,center_x=130 , center_y=50)]

        self.speed = SHIP_SPEED
    
    def rotate(self):
        self.angle += self.change_angle * self.speed
    
    def fire(self):
        arcade.sound.play_sound(self.gun_sound)
        self.bullet_list.append(Bullet(self))  

    def draw(self):
        for h in self.HPs:
            h.draw()  

        return super().draw()    
