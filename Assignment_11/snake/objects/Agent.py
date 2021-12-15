from pyglet.util import Decoder
from  objects.Snake import Snake
import arcade
import math


class Agent(Snake):
    def __init__(self):
        super().__init__()
        self.nearX=0
        self.nearY=0
    
    
    def run(self,game):

        self.get_env(env=game)
        self.set_state(env=game)

    def get_env(self,env):
    
        if math.sqrt((self.center_x-env.apple.apple.center_x)**2+(self.center_y-env.apple.apple.center_y)**2)<\
            math.sqrt((self.center_x-env.pear.pear.center_x)**2+(self.center_y-env.pear.pear.center_y)**2):
            self.nearX=env.apple.apple.center_x
            self.nearY=env.apple.apple.center_y
        else :
            self.nearX=env.pear.pear.center_x   
            self.nearY=env.pear.pear.center_y

    def set_state(self,env):
        
        if  self.center_x>self.nearX:
            env.on_key_release(symbol=arcade.key.LEFT,modifiers=None)
        elif self.center_x <self.nearX:
            env.on_key_release(symbol=arcade.key.RIGHT,modifiers=None)

        elif self.center_y < self.nearY:
            env.on_key_release(symbol=arcade.key.UP,modifiers=None)

        elif self.center_y>self.nearY:
            env.on_key_release(symbol=arcade.key.DOWN,modifiers=None)







