import re
import subprocess
import time

patten = re.compile('\n[\w]+\t')
devices = patten.findall(subprocess.getoutput('adb devices'))

for each in devices:
    subprocess.getoutput('adb -s {0} reboot bootloader'.format(each.strip()))
    time.sleep(5)
