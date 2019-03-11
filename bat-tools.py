import re
import subprocess

print("*******************")
print("*****BAT小工具*****")
print("*******************")

def isConnect():
    Adb_State = subprocess.getoutput("adb get-state")
    if Adb_State == "device":
        print("\n")
        return 1
    else:
        print("Connecte Failed!!,Please Check Again!!")
        print("\n")
        subprocess.getoutput("adb wait-for-device")
    
def getFocusedPackageAndActivity():
    pattern = re.compile(r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+")
    output = subprocess.getoutput("adb shell dumpsys window windows|findstr \/|findstr name=")
    lists = pattern.findall(output)
    component = lists[0]
    print("==========分割线============"+"\n")
    packageName = component.split("/")[0]
    print("1.当前应用包名是:"+packageName)
    return packageName

def getPakacgeVersionName(packageName):
    output = subprocess.getoutput("adb shell dumpsys package " + packageName + "|findstr versionName")
    print("2.当前应用的版本号是:"+output.strip())

def getForChoice():
    choice = int(input("根据需要输入对应ID:\
(1.获取系列号;2.获取IMEI号;3.进入刷机模式;4.获取当前应用的包名和版本;0.退出) "))
    if choice == 1:
        serialno = subprocess.getoutput("adb get-serialno")
        print("==========分割线============")
        print("你选择的是获取系列号:"+serialno)
    elif choice == 2:
        output = subprocess.getoutput("adb shell getprop|findstr imei")
        imei = re.sub(r'[\[\]]',"",output).split("\n")
        print("==========分割线============")
        print("你选择的是获取IMEI号:")
        for each in imei:
            print(each)
    elif choice == 3:
        print("进入fasboot模式")
        subprocess.getoutput("adb reboot bootloader")
    elif choice == 4:
        print("==========分割线============")
        print("获取当前应用包的信息...")
        getPakacgeVersionName(getFocusedPackageAndActivity())
    elif choice == 0:
        print("你选择退出!")
        exit
    else:
        print("\n"+"输入错误,请重试......")
        getForChoice()

if isConnect():
    getForChoice()


        
        
        

