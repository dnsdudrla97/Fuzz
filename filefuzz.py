#-*-coding:utf-8-*-
from pydbg import *
from PyQt5.QtWidgets import QApplication, QWidget
import utils
import random
import sys
import struct
import threading
import os
import shutil
import time
import getopt

class file_fuzzer:
    def __init__(self, exe_path, ext, notify):
        self.exe_path               = exe_path
        self.ext                    = ext
        self.notify_crash           = notify
        self.orig_file              = None
        self.mutated_file           = None
        self.iteration              = 0
        self.exe_path               = exe_path
        self.orig_file              = None
        self.mutated_file           = None
        self.iteration              = 0
        self.crash                  = None
        self.send_notify            = False
        self.pid                    = None
        self.in_accessv_handler     = False
        self.dbg                    = None
        self.running                = False
        self.ready                  = False
        
        # options
        self.smtpserver = 'http://dnsdudrla97.github.io/'
        self.recipients = ['http://dnsdudrla97.github.io/',]
        self.sender     = 'http://dnsdudrla97.github.io/'
        
        self.test_case  = ["%s%n%s%n%s%n%s%n", "\xff", '\x00', "A"] # ramda?

    def file_picker(self):
        file_list = os.listdir("examples/")
        list_length = len(file_list)
        file = file_list[random.randint(0, list_length-1)]
        shutil.copy("examples\\%s" %file, "test.%s" % self.ext)
        return file
    
    def fuzz(self):
        while True:
            if not self.running:
                # 먼저 변형을 가할 파일을 선택
                self.test_file = self.file_picker()
                self.mutate_file()

                # 디버거 스레드를 실행
                pydbg_thread = threading.Thread(target=self.start_debugger)
                pydbg_thread.setDaemon(0)
                pydbg_thread.start()

                while self.pid == None:
                    time.sleep(1)
                
                # 모니터링 스레드를 실행시킨다.
                monitor_thread = threading.Thread(target=self.monitor_debugger)
                monitor_thread.setDaemon(0)
                monitor_thread.start()

                self.iteration +=1
            else:
                time.sleep(1)
    # 대상 애플리케이션을 실행시키는 디버거 스레드





class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())