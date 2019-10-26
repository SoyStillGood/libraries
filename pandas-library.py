import sys
import os
script_name = sys.argv[0]
is_file = os.path.isfile(script_name)
print(is_file)

import time
import random

for i in range(0, 10):
    time.sleep(3)
    print("{} {}".format("input your message here", print(random.randint(0, 50))))

x = 0
argument = sys.argv[1]
while(x<50):
    time.sleep(3)
    print(f'my message {random.randint(0, 500)} user provided {argument}')
