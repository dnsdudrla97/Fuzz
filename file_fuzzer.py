# -*-coding:utf-8-*-
from pydbg import *
from pydbg.defines import *

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

        self.exe_path       = exe_path
        self.ext            = ext
        self.notify_crash   = notify
        self.orig_file      = None
        self.mutated_file   = None
        self.iteration      = 0 
        self.exe_path       = exe_path
        self.orig_file      = None
        self.mutated_file   = None
        self.iteration      = 0
        self.crash          = None
        self.send_notify    = False    
        self.pid            = None
        self.in_accessv_handler = False
        self.dbg            = None
        self.running        = False
        self.ready          = False
        
        # options
        self.smtpserver = 'http://dnsdudrla97.github.io/'
        self.recipients = ['http://dnsdudrla97.github.io/', ]
        self.sender = 'http://dnsdudrla97.github.io/'

        self.test_cases = [ "%s%n%s%n%s%n", "\xff", "\x00", "A", "\x90", "%p", "%n", "%hn", "%hhn"]

    def file_picker( self ):

        file_list = os.listdir("examples/")        
        list_length = len(file_list)
        file = file_list[random.randint(0, list_length-1)]
        shutil.copy("examples\\%s" % file,"test.%s" % self.ext)

        return file


    def fuzz( self ):

        while 1:

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

                self.iteration += 1
    # 대상 애플리케이션을 실행시키는 디버거 스레드
    def start_debugger(self):

        print ("[*] Starting debugger for iteration: %d" % self.iteration)
        self.running = True
        self.dbg = pydbg()

        self.dbg.set_callback(EXCEPTION_ACCESS_VIOLATION,self.check_accessv)
        pid = self.dbg.load(self.exe_path,"test.%s" % self.ext)

        self.pid = self.dbg.pid
        self.dbg.run()         
    # 애플리케이션 몇 초 동안 실행시킨담에 종료시키는 모니터링 스레드
    def monitor_debugger(self):

        counter = 0
        print "[*] Monitor thread for pid: %d waiting." % self.pid,
        while counter < 3:
            time.sleep(1)
            print counter,
            counter += 1

        if self.in_accessv_handler != True:
            time.sleep(1)
            self.dbg.terminate_process()
            self.pid = None
            self.running = False
        else:
            print "[*] The access violation handler is doing its business. Going to sleep"           

            while self.running:
                time.sleep(1)

    # 에러를 추적하고 해당 정보를 저장하기 위한 접근 위반 핸들러
    def check_accessv(self,dbg):

        if dbg.dbg.u.Exception.dwFirstChance:

            return DBG_CONTINUE

        print "[*] Woot! Handling an access violation!"
        self.in_accessv_handler = True
        crash_bin = utils.crash_binning.crash_binning()
        crash_bin.record_crash(dbg)
        self.crash = crash_bin.crash_synopsis()

        # 에러 정보 작성
        crash_fd = open("crashes\\crash-%d" % self.iteration,"w")
        crash_fd.write(self.crash)

        # 파일 백업
        shutil.copy("test.%s" % self.ext,"crashes\\%d.%s" % (self.iteration,self.ext))
        shutil.copy("examples\\%s" % self.test_file,"crashes\\%d_orig.%s" % (self.iteration,self.ext))

        self.dbg.terminate_process()
        self.in_accessv_handler = False
        self.running = False

        if self.notify_crash:
            notify()
            
        return DBG_EXCEPTION_NOT_HANDLED  
    # 에러 정보 이메일 통보
    def notify(self):

        crash_message = "From:%s\r\n\r\nTo:\r\n\r\nIteration: %d\n\nOutput:\n\n %s" % (self.sender, self.iteration, self.crash)

        session = smtplib.SMTP(smtpserver)        
        session.sendmail(sender, recipients, crash_message)
        session.quit()   

        return
    # mutate file
    def mutate_file( self ):

        # 파일의 내용을 버퍼로 읽어들이기
        fd = open("test.%s" % self.ext, "rb")
        stream = fd.read()
        fd.close()


        # 퍼징의 가장 핵심적인 부분
        # 임의의 test_case를 선택해 파일 내부의 임의의 위치에 적용한다.
        test_case = self.test_cases[random.randint(0,len(self.test_cases)-1)]

        stream_length = len(stream)
        rand_offset   = random.randint(0,  stream_length - 1 )
        rand_len      = random.randint(1, 1000)

        # 선택한 test_case를 반복 시킨다.
        test_case = test_case * rand_len

        # 파일 데이터 버퍼에 그것을 삽입한다.
        fuzz_file = stream[0:rand_offset]
        fuzz_file += str(test_case)
        fuzz_file += stream[rand_offset:]

        # 버퍼의 내용을 파일에 써 넣는다.
        fd = open("test.%s" % self.ext, "wb")
        fd.write( fuzz_file )
        fd.close()

        return

def print_usage():

    print "[*]"
    print "[*] file_fuzzer.py -e <Executable Path> -x <File Extension>"
    print "[*]"

    sys.exit(0)

if __name__ == "__main__":

    print "[*] Generic File Fuzzer."

    # 문서 파싱을 수행할 애플리케이션의 경로와 사용될 파일 확장자
    try:
        opts, argo = getopt.getopt(sys.argv[1:],"e:x:n")
    except getopt.GetoptError:
        print_usage()

    exe_path = None
    ext      = None
    notify   = False
    
    for o,a in opts:
        if o == "-e":
            exe_path = a
        elif o == "-x":
            ext = a    
        elif o == "-n":
            notify = True

    if exe_path is not None and ext is not None:
        fuzzer = file_fuzzer( exe_path, ext, notify)
        fuzzer.fuzz()
    else:
        print_usage()