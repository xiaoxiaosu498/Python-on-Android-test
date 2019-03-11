import re
import subprocess

def getConnect():
    Adb_State = subprocess.getoutput("adb get-state")
    if Adb_State == "device":
         print("Connect Succeessfully")
         return 1
    else:
        print("Connect Failed!!,Please Check Again!!")
        subprocess.getoutput("adb wait-for-device")

def getFocusedPackageAndActivity():
    pattern = re.compile(r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+")
    output = subprocess.getoutput(r"adb shell dumpsys window windows|findstr \/|findstr name=")
    lists = pattern.findall(output)
    component = lists[0]
    packageName = component.split("/")[0]
    return packageName

def getPakacgeVersionName(packageName):
    print("1.当前应用包名是:"+packageName)
    version = subprocess.getoutput("adb shell dumpsys package " + packageName + "|findstr versionName")
    print("2.当前应用的版本号是:"+version.strip())
     
def pullFocusedApp(packagename):
    pathInfo = subprocess.getoutput("adb shell dumpsys package " + packagename+"|findstr  path")
    path = pathInfo.split(":")[1].strip()
    #提取应用包
    subprocess.getoutput("adb pull " + path)

if __name__ == "__main__":    
    if getConnect():
        #获取当前应用的包名和版本号
        getPakacgeVersionName(getFocusedPackageAndActivity())
        isPull = input(u"是否需要提取导出?(请选择Y或者N):")
        if isPull in ["Y","y"]:
            pullFocusedApp(getFocusedPackageAndActivity())
            print("Pull成功!")
        else:
            print("你不打算导出App!")
            pass

        




