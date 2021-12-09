import random
import arcade
from objects.Spirtes import *
from objects.Snake import Snake
   

class Env(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH , height=SCREEN_HEIGHT  , title="Snake Game")
        arcade.set_background_color(arcade.color.BLACK_LEATHER_JACKET)
        
        self.snake = Snake()
        self.apple = Apple()
        self.pear = Pear()
        self.hitch = Hitch()
        

    def on_draw(self):
        arcade.start_render()
        if(self.snake.score<0):
            arcade.draw_text('game over :) lol',500,500,arcade.color.WHITE)
        else:
            arcade.draw_text('Score : '+str(self.snake.score),start_x=20 , start_y=40 , font_size=30) 
            self.snake.draw()
            self.apple.draw()
            self.pear.draw()
            self.hitch.draw()
    
    def on_key_release(self, symbol: int, modifiers: int):
        if  symbol == arcade.key.LEFT:
            self.snake.move()
            self.snake.body[-1][0]-=20
            self.check_pos()
            
        elif symbol == arcade.key.RIGHT:
            self.snake.move();
            self.snake.body[-1][0]+=20
            self.check_pos()

        elif symbol == arcade.key.UP:
            self.snake.body[-1][1]+=20
            self.snake.move();
            self.check_pos()

        elif symbol == arcade.key.DOWN:
            self.snake.body[-1][1]-=20
            self.snake.move();
            self.check_pos()
            
    def check_pos(self):
        
        if arcade.check_for_collision(self.snake,self.apple.apple):
            self.snake.eat('apple')
            self.apple= Apple()
        
        elif arcade.check_for_collision(self.snake,self.pear.pear):
            self.snake.eat('pear')
            self.pear = Pear()
            
        elif arcade.check_for_collision(self.snake,self.hitch.hitch):
            self.snake.eat('shit')
            self.hitch = Hitch()
            





my_game = Env()
arcade.run()