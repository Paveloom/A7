import sys
from time import sleep

for x in range(10):
    sys.stdout.write("\r%d" % x)
    sleep(1)
print("\n")