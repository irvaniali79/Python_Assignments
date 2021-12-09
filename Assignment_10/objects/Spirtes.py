import arcade
import random
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.image = 'assets/apple.png'
        self.apple = arcade.Sprite(self.image, 0.10)
        self.apple.center_x  = random.randrange(60, SCREEN_HEIGHT , 20) 
        self.apple.center_y  = random.randrange(60, SCREEN_WIDTH , 20) 

    def draw(self):
        self.apple.draw()

class Pear(arcade.Sprite):
     def __init__(self):
        super().__init__()
        self.image = 'assets/pear.png'
        self.pear = arcade.Sprite(self.image, 0.04)
        self.pear.center_x  = random.randrange(60, SCREEN_HEIGHT , 20) 
        self.pear.center_y  = random.randrange(60, SCREEN_WIDTH , 20) 

     def draw(self):
        self.pear.draw()  

class Hitch(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.image = 'assets/shit.png'
        self.hitch = arcade.Sprite(self.image, 0.08)
        self.hitch.center_x  = random.randrange(60, SCREEN_HEIGHT , 20) 
        self.hitch.center_y  = random.randrange(60, SCREEN_WIDTH , 20) 

    def draw(self):
        self.hitch.draw()