import os
# 递归查询一个目录
def qurey_file(path):
    #path = "G:\搬家\桌面\所有\正式上课\Mysql\day04"
    for path,dirs,file in os.walk(path):
        for path_file in file:
            yield path+os.sep+path_file
# 读取有几个盘符
def get_drive():
    drive = []
    for i in range(65,91):
        vol = chr(i) + ':'
        if os.path.isdir(vol):
            drive.append(vol)
    return drive
#qurey_file("G:\搬家\桌面\所有\正式上课\Mysql\day04")
#get_drive()