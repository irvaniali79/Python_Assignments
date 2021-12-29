from objects.Spacecraft import Spacecraft 
from objects.Enemy import Enemy
from config.config import *
import time
import threading

class MyGame(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.ship=Spacecraft();
        self.score=0
        
        self.enemy_list=[]
    

        self.set_mouse_visible(False)

        self.end_th=False
        self.my_thread=threading.Thread(target=self.add_enemy,args=(lambda:self.end_th,)) 
        self.my_thread.start()
        
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(":resources:images/backgrounds/stars.png")

    def add_enemy(self,stop):
        while True:
            self.enemy_list.append(Enemy())
            time.sleep(5)
            if stop():
                break
          
    def on_draw(self):
        arcade.start_render()
        if(not(len(self.ship.HPs))):
            arcade.draw_text('game over :) lol',SCREEN_WIDTH//2,SCREEN_HEIGHT//2,arcade.color.WHITE,width=400, align='center')
            self.end_th=True
            self.close()
        else:
          
            self.ship.draw();
            self.ship.bullet_list.draw()

            for i in range(len(self.enemy_list)):
                self.enemy_list[i].draw()

            arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background_image)
            arcade.draw_text(f"Score: {self.score}",SCREEN_WIDTH-80 , 30, arcade.color.WHITE, width=14)


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

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].update()
                
        for enemy in self.enemy_list:
            if(arcade.check_for_collision(self.ship,enemy)):
                enemy.hit()
                self.enemy_list.remove(enemy)
                hp=self.ship.HPs.pop()
                hp.remove_from_sprite_lists()
            if enemy.top < 0:
                self.enemy_list.remove(enemy)
                hp=self.ship.HPs.pop()
                hp.remove_from_sprite_lists()

        for bullet in self.ship.bullet_list:
            for enemy in self.enemy_list:
                if(arcade.check_for_collision(bullet,enemy)):
                    self.score += 1
                    enemy.hit()
                    self.enemy_list.remove(enemy)   
                
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
