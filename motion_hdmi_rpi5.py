from gpiozero import MotionSensor
from signal import pause
import subprocess
import time

pir = MotionSensor(23)

def motion_function():
    #print("Motion Detected")
    subprocess.call("sh /home/pi/mon.sh", shell=True)
    time.sleep(120)
    
def no_motion_function():
    #print("Motion stopped")
    subprocess.call("sh /home/pi/mof.sh", shell=True)

pir.when_motion = motion_function
pir.when_no_motion = no_motion_function

pause()