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
    def start_debugger(self):
        print("[*] Starting debugger for iteration: %d" % self.iteration)
        self.running = True
        self.dbg = pydbg()   

        self.dbg.set_callback(EXCEPTION_ACCESS_VIOLATION, self.check_accessv)
        pid = self.dbg.load(self.exe_path, "test.%s" % self.ext)

        self.pid = self.dbg.pid
        self.dbg.run()
    
    # 에러를 추적하고 해당 정보를 저장하기 위한 접근 위반 핸들러
    def check_accessv(self, dbg):
        if dbg.dbg.u.Exception.dwFirstChance:
            return DBG_CONTINUE
        print("[*] Woot! Handling an access violation!")
        self.in_accessv_handler = True
        crash_bin = utils.crash_binning.crash_binning()
        crash_bin.record_crash(dbg)
        self.crash = crash_bin.crash_synopsis()
    
        # 에러 정보 작성
        crash_fd = open("crashes\\crash-%d" % self.iteration, 'w')
        crash_fd.write(self.crash)

        # 파일 백업
        shutil.copy("test.%s" % self.ext, "crashes\\%d.%s" % (self.iteration, self.ext))
        shutil.copy("examples\\%s" % self.test_file, "crashes\\%d_orig.%s" % (self.iteration, self.ext))
        self.dbg.terminate_process()
        self.in_accessv_handler = False
        self.running = False
        return DBG_EXCEPTION_NOT_HANDLED
    
    # 애플리케이션 몇 초 동안 실행시킨담에 종료시키는 모니터링 스레드
    def monitor_debugger(self):
        counter = 0
        print("[*] Monitor thread for pid: %d watting." % self.pid)
        
        while counter < 3:
            time.sleep(1)
            print(counter)
            counter += 1
        
        if self.in_accessv_handler != True:
            time.sleep(1)
            self.dbg.terminate_process()
            self.pid = None
            self.running = False
        else:
            print("[*] The access violation handler is doing its business. Waiting")

            while self.running:
                time.sleep(1)
    # 에러 정보 이메일 통보
    def notify(self):
        crash_message = "From:%s\r\n\r\nTo:\r\n\r\nIteration:%d\n\nOutput:\n\n %s" % (self.sender, self.iteration, self.crash)
        session = smtplib.SMTP(smtpserver)
        session.sendmail(sender, recipients, crash_message)
        session.quit()
        return
        








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