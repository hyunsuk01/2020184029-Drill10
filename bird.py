from random import randint

from pico2d import load_image

import game_framework

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    action = None
    dir = 0
    x = randint(200, 1400)
    frame = 0
    image = None

    def __init__(self, x=randint(200, 1400), y=randint(100, 500)):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y

    def draw(self):
        Bird.frame = (Bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        Bird.x += Bird.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1500:
            self.image.clip_composite_draw(int(Bird.frame) * 100, Bird.action * 100, 100, 100, 0, '', self.x, self.y,
                                           200, 200)
        elif self.x < 100:
            self.image.clip_composite_draw(int(Bird.frame) * 100, Bird.action * 100, 100, 100, 0, 'v', self.x, self.y,
                                           200, 200)

    def update(self):
        pass
