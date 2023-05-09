from random import randint
import subprocess
ran1 = randint(11,99)
ran2 = randint(11,99)
ran3 = randint(11,99)
ran4 = randint(11,99)
ran5 = randint(11,99)
ran6 = randint(11,99)


subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call(f"ifconfig wlan0 hw ether {ran1}:{ran2}:{ran3}:{ran4}:{ran5}:{ran6}", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)