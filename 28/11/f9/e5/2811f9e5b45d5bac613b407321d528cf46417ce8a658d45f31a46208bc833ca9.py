import time
import os
import random

base_time = 30
random_range = 15

names = ['vim', 'gedit', '/usr/lib/firefox/firefox']


def kill_one():
    os.system('killall {}'.format(random.choice(names)))


while True:
    kill_one()
    restart = base_time + random.random() * random_range - random_range / 2
    time.sleep(restart)
