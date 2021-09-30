import arcade
import pathlib
import AnimatedSpriteWindow


FRAME_HEIGHT = 512
FRAME_WIDTH = 512


def main():
    window = AnimatedSpriteWindow.AnimatedSpriteWindow()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()