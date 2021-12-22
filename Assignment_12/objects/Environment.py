from objects.Spacecraft import Spacecraft 
from objects.Enemy import Enemy
from config.config import *
import time

class MyGame(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.ship=Spacecraft();
        self.score=0
        
        self.enemy_list=arcade.SpriteList()

        self.set_mouse_visible(False)
 
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(":resources:images/backgrounds/stars.png")
        arcade.schedule(self.spawner,1)
    def spawner(self,_):
        self.enemy_list.append(Enemy())


    def on_draw(self):
        arcade.start_render()
        if(not(len(self.ship.HPs))):
            arcade.draw_text('game over :) lol',SCREEN_WIDTH//2,SCREEN_HEIGHT//2,arcade.color.WHITE,width=400, align='center')
            
        else:
            self.ship.draw();
            self.ship.bullet_list.draw()
            self.enemy_list.draw()
    
            arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background_image)
            arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.ship.center_x = x
        self.ship.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        self.ship.fire();

    def on_key_press(self, symbol: int, modifiers: int):
       
        if symbol == arcade.key.LEFT:
            self.ship.change_angle = 5
            self.ship.rotate()  

        elif symbol == arcade.key.RIGHT:
            self.ship.change_angle = -5    
            self.ship.rotate()

    def on_update(self, delta_time):
        self.ship.bullet_list.update()
        self.enemy_list.update()

        for enemy in self.enemy_list:
            if(arcade.check_for_collision(self.ship,enemy)):
                enemy.hit()
                enemy.remove_from_sprite_lists()
                hp=self.ship.HPs.pop()
                hp.remove_from_sprite_lists()
            if enemy.top < 0:
                enemy.remove_from_sprite_lists()
                hp=self.ship.HPs.pop()
                hp.remove_from_sprite_lists()

        for bullet in self.ship.bullet_list:
            for enemy in self.enemy_list:
                if(arcade.check_for_collision(bullet,enemy)):
                    self.score += 1
                    enemy.hit()
                    enemy.remove_from_sprite_lists()   
                
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
