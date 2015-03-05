# -*- coding:utf-8 -*-
"""
SendMessage to QQ
You most install QQ and login it.
cmd arg:
-qq_number:
-text:
like:
qqmsg.exe 394452216 hellow

join
"""

import win32gui
import time
import sys
import os
import win32clipboard as w
import win32con
import win32api

def setImage(path=None):
    win32api.keybd_event(44,0,0,0)
    win32api.keybd_event(44,0,win32con.KEYEVENTF_KEYUP,0)

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def show_qq_by_number(number):
    key = win32api.RegOpenKey(win32con.HKEY_CLASSES_ROOT, '\\Tencent\\DefaultIcon',0, win32con.KEY_ALL_ACCESS)
    qq_path = win32api.RegQueryValue(key,'') 
    command = '"{exe_path}" {arg}' .format(exe_path=qq_path[:-2],arg=' tencent://message/?uin=' +str(number))
    os.system(command)

def send_message():
    win32api.keybd_event(17,0,0,0)
    time.sleep(0.05)
    win32api.keybd_event(86,0,0,0)
    time.sleep(0.05)
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.05)
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.05)

    win32api.keybd_event(18,0,0,0)
    time.sleep(0.05)
    win32api.keybd_event(83,0,0,0)
    time.sleep(0.05)

    win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.05)
    win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.05)

if len(sys.argv) > 2:
    qq, text = sys.argv[1], sys.argv[2]
    show_qq_by_number(qq)
else:
    text = u'-'*20

#set text with unicode
setText(text.decode('gbk'))
send_message()
