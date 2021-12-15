from pyglet.util import Decoder
from  objects.Snake import Snake
import arcade
import math


class Agent(Snake):
    def __init__(self):
        super().__init__()
    
    
    def run(self,game):
        self.get_env(env=game)
        self.set_state(env=game)

    def get_env(self,env):
    
        if math.sqrt((env.snake.center_x-env.apple.center_x)**2+(env.snake.center_y-env.apple.center_y)**2)<\
            math.sqrt((env.snake.center_x-env.pear.center_x)**2+(env.snake.center_y-env.pear.center_y)**2):
            self.nearX=env.apple.center_x
            self.nearY=env.apple.center_y
        else :
            self.nearX=env.pear.center_x   
            self.nearY=env.pear.center_y

    def set_state(self,env):

        if  self.snake.center_x>X:
            env.on_key_release(symbol=arcade.key.LEFT,modifiers=None)

        elif self.snake.center_x <X:
            env.on_key_release(symbol=arcade.key.RIGHT,modifiers=None)

        elif self.snake.center_y < Y:
            env.on_key_release(symbol=arcade.key.UP,modifiers=None)

        elif self.snake.center_y>Y:
            env.on_key_release(symbol=arcade.key.DOWN,modifiers=None)







