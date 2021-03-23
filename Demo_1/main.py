from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import (NumericProperty, ReferenceListProperty,
    ObjectProperty,ListProperty,StringProperty)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import *
from kivy.config import Config

#importing self made classes
from Tile import Tiles
from Non_widget_class import add_score,lose_life
import random

Builder.load_file('style.kv')
#Window.size = (1920,1080)

class GameOverButton(Widget):
    pass

#creating the main gameplay
class GameScreen(Widget):

    #creating a list to store widgets
    tile_list = ListProperty([])
    score = ObjectProperty(None)
    life = ObjectProperty(None)
    #reset button object property
    #reset = ObjectProperty(None)

    # def __init__(self, **kwargs):
    #     super(GameScreen, self).__init__(**kwargs)
    #     #excitedly creating and testing how defing widgets work

    def new_game(self):
        #print(self.ids.new_game_btn)

        try:
            self.remove_widget(self.ids.new_game_btn)#getting the button id, kivy cant delete children of children

        except:
            #retry += 1
            print("again ")

        self.skippy = Clock.schedule_interval(self.rnd_spawing,.5)
        self.jhonny = Clock.schedule_interval(self.update,1/30)
        #- testing
        self.score.text = 'Score: 0'
        self.life.text = "Life: 5"
        #lose_life(self.life)

    def update(self,dt):
        #-debugging
        #print(dt)
        #print('printing rand int: ',rnd_int)
        #print('head obj num: ',self.tile_list[0].number)

        #- updating the tile list head
        if not self.tile_list:
            #print('no tiles')
            pass
        else:
            self.head = self.tile_list[0] #defining lead tile every update
            #- checking collision with top of screen
            if self.head.pos[1] >= Window.height:
                self.remove_widget(self.head)
                self.tile_list.remove(self.head)
                print('deleted head lose a turn ',self.head.number)
                lose_life(self.life)

        #- checking if the value of score is 0
        if int(self.life.text[self.life.text.find(' ')+1:len(self.life.text)]) <= 0:
            ### if score == 0 clears everything
            self.skippy.cancel()
            self.jhonny.cancel()
            for i in self.tile_list:
                self.remove_widget(i)
            self.tile_list = []
            #self.add_widget(self.ids.new_game_btn)
            self.add_widget(GameOverButton())


    #- spawns a tile at random color
    def rnd_spawing(self,dt):
        rnd_int = random.randint(1,4) #creating random int
        new_tile = Tiles(rnd_int) #creating tile with random int
        self.add_widget(new_tile)
        self.tile_list.append(new_tile) #adding to list

    #deleting head widget in list
    def del_tile(self,btn_num):
        #-debugging button number
        #print('button num: ',btn_num)
        #print('list num',self.tile_list[0].number)

        #checking if the list is empty
        if len(self.tile_list) <= 0:
            lose_life(self.life)
            print('nothing in list') #lose a point for pressing button with no tiles
        #otherwise checkeing if the correct button was pressed
        else:
            if self.head.number == btn_num: #if lead tile's number is the same as the btn pressed
                #print('shiiit') #need to substiture for other functions
                self.remove_widget(self.tile_list[0])
                self.tile_list.remove(self.tile_list[0])
                add_score(self.score)
            else:
                #losing point for getting color wrong
                lose_life(self.life)

#the app class
class SortApp(App):
    #creating main function
    def build(self):
        self.game = GameScreen()
        #print(game.ids.life)
        return self.game

    #create other function that takes in an object
    def reset_game_app(self):
        self.game.remove_widget(self.game.children[0])
        self.game.new_game()
        #print(self.game.children.some_id)
        print(self.game.children[0])
        # for i in self.game.children.__main__:
        #     print(i)




if __name__ == '__main__':
    SortApp().run()
