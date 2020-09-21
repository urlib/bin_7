import os
import time
os.chdir(os.path.dirname(os.path.abspath(__file__)))

while True:
    os.system('python fake_nord.py')
    time.sleep(0.5)
