import re
import os
import subprocess
import platform

#lambda函数返回path规范化的绝对路径。
PATH = lambda p: os.path.abspath(p)

system = platform.system()
if system is "Windows":
    find_util = "findstr"
else:
    find_util = "grep"

def get_current_package_name():
    pattern = re.compile(r'[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+')
    subprocess.getoutput("adb wait-for-device")
    output = subprocess.getoutput('adb shell dumpsys window windows|{0} \/|{1} name='.format(find_util,find_util))
    package_name = pattern.findall(output)[0].split("/")[0]
    return package_name

def get_match_apk(package_name,path):
    pathInfo = subprocess.getoutput("adb shell dumpsys package {}|{} path".format(package_name,find_util))
    path_home = pathInfo.split(":")[1].strip()
    subprocess.getoutput("adb pull {} {}".format(path_home, path))

if __name__ == "__main__":
    path = PATH(os.getcwd()+"/Apps")
    if not os.path.isdir(path):
        os.makedirs(path)
    else:
        get_match_apk(get_current_package_name(), path)

    