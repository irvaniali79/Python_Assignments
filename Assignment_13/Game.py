from arcade.application import Window
from objects.Environment import MyGame
from config.config import *

def main():
    window = MyGame()
    window.center_window()
    arcade.run()


if __name__ == "__main__":
    main()