from pysql import mysqlpython
from search import qurey_file, get_drive
import multiprocessing
import threading
import time
import qt
from threading import *
import PyHook3
import pythoncom
import time



def OnKeyboardEvent(event):
    global t1
    if event.Key != 'Escape':
        if time.time() - t1 < 0.5:
            if event.Key == 'Lmenu':
                qt.dis.run()
            t1 = 0
        else:
            t1 = time.time()
    else:
        qt.dis.stop()
    return True

# 按键监听
def key_listen():
    global t1
    t1 = 0
    # create the hook mananger
    hm = PyHook3.HookManager()
    # register two callbacks
    # hm.MouseAllButtonsDown = OnMouseEvent
    hm.KeyDown = OnKeyboardEvent
    # hook into the mouse and keyboard events
    # hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()

# 建立索引
def build_index(paths):
    sql = connect_mysql()
    for value in qurey_file(paths):
        # print(value)
        try:
            sql.insert_data(sql.table_name, value)
        except 1062 as f:
            pass
            # print("f",f)
    sql.close()


# 任务表
def task(paths):
    while True:
        build_index(paths)
        time.sleep(120)



# 连接mysql
def connect_mysql():
    sql = mysqlpython("localhost", 3306, "root", "tarena", charset="utf8")
    sql.create_db()
    sql.create_table()
    return sql

def search():
    while True:
        if qt.dis.text != None:
            print(qt.dis.text)
            sql.data_range(sql.table_name, qt.dis.text)
            qt.dis.text = None


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=12)
    for i in get_drive():
        pool.apply_async(task, (i,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
    pool.apply_async(key_listen)
    pool.close()
    #sql = connect_mysql()
    # sql.clear_table(sql.table_name)

    while True:
        search()
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
