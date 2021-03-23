from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty,ListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import *

Builder.load_file('Tile.kv')

#creating all the spawnable Tile widgets
class Tiles(Widget):

    #creating all speed parameters
    speed = -25
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(speed)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    #creating list properties of the colors going to be used
    red = ListProperty([1,0,0])
    green = ListProperty([0,1,0])
    yellow = ListProperty([1,1,0])
    blue = ListProperty([0,0,1])

    #using the super on the init to override default vals
    def __init__(self,number, **kwargs):
        super(Tiles,self).__init__(**kwargs)
        self.number = number #using number to generate random property
        #defining spawn postion
        self.x_pos = Window.width/2 - self.width #drawing squares in the center
        self.y_pos = 800 #to appear off screen
        self.pos = (self.x_pos, self.y_pos) #kivy widget already have a self.pos im respecifying theirs to equal my own values of x and y otherwise will default to (0,0)
        self.size = (200,200) #overwriting default size like the previous set
        Clock.schedule_interval(self.move,1/30) #schedualing the move function as its initialized
        self.rnd_color() #updateing values of the canvas to specified color


    #
    def rnd_color(self):
        #on instantiation defining the color it will be
        if self.number == 1:
            with self.canvas.before:
                Color(rgb=self.red)
        elif self.number == 2:
            with self.canvas.before:
                Color(rgb=self.blue)
        elif self.number == 3:
            with self.canvas.before:
                Color(rgb=self.green)
        else:
            with self.canvas.before:
                Color(rgb=self.yellow)


    def move(self,dt):
        #vector math to make the widget move once instantiated
        self.pos=Vector(*self.velocity) + self.pos
