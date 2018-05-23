#read file system!
# ------------------
#import Sepor
#import View
#import Controller

import time
import os

time.sleep(1)
print("5")

import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

sys.exit()