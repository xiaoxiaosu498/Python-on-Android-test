import subprocess

pkg_list = subprocess.getoutput("adb shell pm list package -3").replace("package:","").split("\n")

count = 1
for each in pkg_list:
    path = subprocess.getoutput("adb shell pm path "+ each).split(":")[1]
    subprocess.getoutput("adb pull " + path)
    print("成功获取第%d个App" % count)
    count +=1

print("总共获取%d个三方App,已全部获取!!" % int(count-1))
