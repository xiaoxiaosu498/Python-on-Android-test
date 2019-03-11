import subprocess
import platform
import time


system = platform.system()
if system == "Windows":
    find_util = "findstr"
else:
    find_util = "grep"

#root device
hone = 0
camera = 0

cameraserver_pid = subprocess.getoutput('adb shell ps -A|{} cameraserver'.format(find_util)).split(')[1]
home_activity = 'com.bbk.launcher2/com.bbk.launcher2.Launcher'
camera_activity = 'com.android.camera/com.android.camera.CameraActivity'

bright_node = 'sys/class/leds/lcd-backlight/brightness'
brightness = subprocess.getoutput('adb shell cat {}'.format(bright_node))

print('cameraserver_pid {}'.format(cameraserver_pid))
print('brightness is {}'.format(brightness))

if brightness == 0:
    print("Power on the screen")
    subprocess.getoutput('adb shell input keyevent 26')
    time.sleep(5)

while home == 0:
    top_activity  = subprocess.getoutput('adb shell dumpsys activity top|{} ACTIVITY'.format(find_util))
    time.sleep(1)

if 