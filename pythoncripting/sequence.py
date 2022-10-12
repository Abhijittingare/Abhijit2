import subprocess
import time


def MyFunc():
    time.sleep(5)

    print("My file is saved")

    subprocess.Popen (['C:\\Windows\\notepad.exe', 'my text.txt'], shell=True) 
    print("I can view the file")
    print('Create a text file.')
    fileObj = open('mytext.txt', 'w')
    fileobj.write('My Text file!')
    fileobj.close
    threadObj = threading. Thread (target=MyFunc) threadObj.st
    print('Program Over')