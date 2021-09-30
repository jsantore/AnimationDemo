import arcade
import pathlib
from typing import List
from main import FRAME_WIDTH, FRAME_HEIGHT


class AnimatedSpriteWindow(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Demo animation")
        self.coin_sprite = None
        self.think_list = None

    def update(self, delta_time: float):
        self.coin_sprite.update_animation()

    def on_draw(self):
        arcade.start_render()
        self.thing_list.draw()

    def setup(self):
        path = pathlib.Path.cwd() / 'Assets' / 'Coin_Spin_Animation_A.png'
        self.coin_sprite = \
            arcade.AnimatedTimeBasedSprite(path, 0.75, center_x=300, center_y=300)
        coin_frames: List[arcade.AnimationKeyframe] = []
        for row in range(4):
            for col in range(4):
                frame = \
                    arcade.AnimationKeyframe(col * row, 50, arcade.load_texture(str(path),
                                                                                 x=col * FRAME_WIDTH,
                                                                                 y=row * FRAME_HEIGHT,
                                                                                 width=FRAME_WIDTH,
                                                                                 height=FRAME_HEIGHT))
                coin_frames.append(frame)
        self.coin_sprite.frames = coin_frames
        self.thing_list = arcade.SpriteList()
        self.thing_list.append(self.coin_sprite)