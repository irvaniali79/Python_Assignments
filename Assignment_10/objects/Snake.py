import arcade
from objects.Spirtes import *

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.change_x = None
        self.change_y = None
        self.score = 0
        self.body=[[SCREEN_WIDTH //2,SCREEN_HEIGHT //2,30,30,arcade.color.GREEN,None,None]]

    def move(self):

        self.body[-1][5]=    self.body[0][0]
        self.body[-1][6]=    self.body[0][1]
        self.body[-1][0]=   self.body[0][0]
        self.body[-1][1]=   self.body[0][1]
        tmp=self.body[-1]
        self.body.pop(-1)
        self.body.insert(0,tmp)

    def eat (self , obj_type):
            if obj_type == 'apple':      
                self.score = self.score + 1
                self.body.append([ self.body[-1][5],self.body[-1][6],30,30,arcade.color.GREEN,None,None])
                return True
            elif obj_type == 'pear':
                self.score = self.score + 2
                self.body.append([ self.body[-1][5],self.body[-1][6],30,30,arcade.color.GREEN,None,None])
                if(self.body[-1][0]==self.body[-2][0]):
                    if(self.body[-1][1]>self.body[-2][1]):
                        self.body.append([ self.body[-1][0],self.body[-1][1]+20,30,30,arcade.color.GREEN,None,None])
                        self.body[-1][5]=self.body[-1][0]
                        self.body[-1][6]=self.body[-1][1]+20
                    else:
                        self.body.append([ self.body[-1][0],self.body[-1][1]-20,30,30,arcade.color.GREEN,None,None])
                        self.body[-1][5]=self.body[-1][0]
                        self.body[-1][6]=self.body[-1][1]-20
                elif(self.body[-1][1]==self.body[-2][1]):
                    if(self.body[-1][0]>self.body[-2][0]):
                        self.body.append([ self.body[-1][0]+20,self.body[-1][1],30,30,arcade.color.GREEN,None,None])
                        self.body[-1][5]=self.body[-1][0]+20
                        self.body[-1][6]=self.body[-1][1]
                    else:
                        self.body.append([ self.body[-1][0]-20,self.body[-1][1],30,30,arcade.color.GREEN,None,None])
                        self.body[-1][5]=self.body[-1][0]-20
                        self.body[-1][6]=self.body[-1][1]
                return True 
            elif obj_type == 'shit':
                if(self.score<0):
                    return False

                self.score = self.score - 1  
                self.body.pop(-1)
                return True       

    def draw (self):
        for knuckle in self.body:
            arcade.draw_rectangle_filled(knuckle[0],knuckle[1],knuckle[2],knuckle[3],knuckle[4])
              
