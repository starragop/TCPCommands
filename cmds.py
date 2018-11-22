import os

def power(cmd):
    if cmd == "shutdown":
        os.system("shutdown -s now")
    elif cmd == "restart":
        os.system("shutdown -r now")

def prnt(text):
    print(text)
