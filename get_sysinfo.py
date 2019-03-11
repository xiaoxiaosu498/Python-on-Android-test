from subprocess import getoutput
from re import sub


sysinfo = getoutput('adb shell "getprop|grep product"')
sysinfo = sub(r"[\[\]]","",sysinfo)

sysinfo_items = sysinfo.split('\n')

for each in sysinfo_items:
    if "ro.vivo.product.version" in each:
        print("该手机的版本是：%s" % each.split(":")[1])
    elif "platform" in each:
        print("该手机的平台是：%s" % each.split(":")[1])
    elif "ro.vendor.product.model" in each:
        print("该手机的型号是：%s" % each.split(":")[1])

input()