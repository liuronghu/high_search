import PyHook3
import pythoncom
import schedule
import time


t1 = 0
key_flag = None
def OnKeyboardEvent(event):
    global key_flag
    print('key',key_flag,type(key_flag))
    if event.Key != 'Escape':
        if time.time() - t1 < 0.5:
            if event.Key == 'Lmenu':
                print('Lmenu')
                key_flag = 'Lmenu'
            t1 = 0
        else:
            t1 = time.time()
    else:
        print('esc')
        key_flag = 'esc'
    return True

# 按键监听
def key_listen():
    # create the hook mananger
    hm = PyHook3.HookManager()
    # register two callbacks
    # hm.MouseAllButtonsDown = OnMouseEvent
    hm.KeyDown = OnKeyboardEvent

    # hook into the mouse and keyboard events
    # hm.HookMouse()
    hm.HookKeyboard()

    pythoncom.PumpMessages()


