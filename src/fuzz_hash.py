# -*- coding: utf-8 -*-
from pydbg import *
from pydbg.defines import *
from ctypes import *
from operator import itemgetter
import mimetypes
import mimetools
import urllib2
import cookielib
import optparse
import os
import sys
import utils
import random
import threading
import shutil
import time
import pickle
import hashlib
import re

# pyqt4
from PyQt4.QtGui import *
import sys
import main_

class file_fuzzer(QDialog, main_.Ui_Dialog):
	def __init__(self, targetProgram, sampleFolder):
		
		# pyqt gui init
		QDialog.__init__(self)
		self.setupUi(self)

		# fuzz init
		self.programPath = targetProgram		 # Target program full path
		self.sampleFolder = sampleFolder	     # Folder with samples to be transformed
		self.ext = ""					         # target format
		self.copyFile = "test"				     # target copy
		self.runTime = 4					     # run time
		self.programCount = 0			 	     # Variable to store the number of program executions
		self.mutateDic = {}				         # mutate info 
		self.pid = None				     	     # pid
		self.crashHandler = False	             # crash handler
		self.dbg = None						     # dbg
		self.running = False				     # running 
		self.stream = None
		self.crashBin = None
		self.crashData = None # event to class -> mainDialog
		self.badChar = ["\x00", "\x41", "\xff", "\x0c", "\xAA"]
		self.badVector = [[os.urandom(4), os.urandom(4), os.urandom(4), os.urandom(4), os.urandom(4), "\x00\x00\x00\x00", "\xff\xff\xff\xff", ],
                     ["A"*5, "A"*17, "A"*33, "A"*65, "A"*129, "A"*257, "A" *513, "A"*1024, "A"*2049, "A"*4097, "A"*8193, "A"*12288, ],
                     ["%99n", "%s%p%x%d", ".1024d", "%.2049d", "%n%n", "%p%p", "%x%x", "%d%d", "%s%s", "%99999999999s", "%08x", "%%20d",
                     	"%%20n", "%%20x", "%%20s", "%#0123456x%08x%x%s%p%d%n%o%u%c%h%l%q%j%z%Z%t%i%e%g%f%a%C%S%08x%%", "%s"*129, "%x"*257, ],
                     ["\x3f\xff", "\xff\x3f", "\x7f\xff", "\xff\x7f","\x80\x00", "\x00\x80", "\xfe\xff", "\xff\xfe", ],
                     ["\x00\x00\x01\x00", "\x00\x01\x00\x00", "\x00\x00\x10\x00", "\x00\x01\x00\x00", "\x00\x00\x01\x00", "\x00\x10\x00\x00", "\x3f\xff\xff\xff", "\xff\xff\xff\x3f", "\x7f\xff\xff\xfe", "\xfe\xff\xff\x7f", "\x7f\xff\xff\xff", "\xff\xff\xff\x7f", "\x80\x00\x00\x00", "\x00\x00\x00\x80", "\xff\xff\xff\xfe", "\xfe\xff\xff\xff", ]]
	'''

	'''
	def fuzz(self):
		'''Returns If there is no sample folder, return
		Args :				
		Returns:			
			If there is no sample folder, return
		'''
		while 1:
			if not self.running:
				self.clearFile()											   # caller tmp file (clear)

				self.programCount += 1
				try:
					file_list = os.listdir(self.sampleFolder)				   # Made the list
				except:
					print "[-] %s folder does not exist." % self.sampleFolder
					return
				
				list_length = len(file_list)
				self.targetfile = file_list[random.randint(0, list_length-1)]  # Target file Select

				fd = open(self.sampleFolder+"/%s" % self.targetfile, "r+b")    # Target file Open(r+b)
				self.ext = self.targetfile[-4:]								   # Save the Target file EXT
				self.stream = fd.read()										   # Save the Target file Stream
				fd.close()
				self.mutationFile()											   # Mutate Target file caller

				try:
					self.dbg.terminate_process()                               
				except:
					pass

				#startDebugger Method Thread start
				pydbg_thread = threading.Thread(target=self.startDebugger)
				pydbg_thread.setDaemon(0)
				pydbg_thread.start()

				counter = 0
				while self.pid == None:
					if counter < 5:
						time.sleep(1)
						counter = counter+1
						if counter >= 5:
							break
				if self.pid == None:
					print "[-] WARNNING!"

				#monitorDebugger Method THread start
				monitor_thread = threading.Thread(target=self.monitorDebugger)
				monitor_thread.setDaemon(0)
				monitor_thread.start()
			else:
				time.sleep(1)
	
	# clear file -> _INIT_
	def clearFile(self):
		'''
		clear tmp file		
		'''
		try:
			os.remove(".esp.log")
		except:
			pass
		try:
			os.remove("crashAllInfo.txt")
		except:
			pass
		try:
			os.remove(".hash.log")
		except:
			pass
		try:
			os.remove(".tmp_MutateDic.txt")
		except:
			pass
		return


	# Fuzz.Mutate Target file
	def mutationFile(self):
		'''
		doc : Testcase creation and mutation work based on seed value
		return :
			1. file error
			2. mutation loop finish

		'''
		self.mutateDic = {}									                            # Reset Mutate key

		try:
			copyFd = open(self.copyFile+self.ext, "w+b")	                            # Copy File Open(w+b)
			copyFd.write(self.stream)						                            # Save the File Stream
			print "[-] Mutate %s" % self.targetfile,	
		except:
			print "[-] File Copy Failed"
			return

		# The mutate counter is based on the Full length 
		streamLength = len(self.stream)					                                # Get the Full length of the target file
		mutateCount = int(streamLength*0.01)
		mutateCount2 = int(streamLength*0.0001)

		# Mutate 1
		for i in range(mutateCount):
			randOffsetStart = random.randint(0, streamLength-1)				            # Random starting position
			# Random starting position + 1~4 Byte
			randOffsetEnd = randOffsetStart+random.randrange(1, 5)
			streamRand = self.stream[randOffsetStart:randOffsetEnd].encode("hex")       # Save the Position stream
			streamLen = len(streamRand)/2											    # Save the Stream length
			badChar = random.choice(self.badChar) * streamLen						    # Choose a bad Character
			# Move the file descriptor pointer
			copyFd.seek(randOffsetStart)
			copyFd.write(badChar)													    # Bad character is stored in the stream
			# Create dictionary for recovery
			self.mutateDic[randOffsetStart] = streamRand

		# Mutate 2
		for i in range(mutateCount2):
			# Random starting position
			randOffset = random.randint(0,  streamLength - 1)
			randVector = random.choice(random.choice(self.badVector))				   # Choose a bad vector
			# print "randVector : %s" % randVector
			randLen = len(randVector)											       # Save the vector length
			copyFd.seek(randOffset)												       # Move the file descriptor pointer

			# Bad character is stored in the stream
			copyFd.write(randVector)

			# Create dictionary for recovery
			self.mutateDic[randOffset] = self.stream[randOffset:randOffset +randLen].encode("hex")	
		copyFd.close()
		return

	# fuzz start debugger
	def startDebugger(self):
		'''
		doc : Start binary debugging, call checkCrash function when vulnerability is detected
		return : pid is none
		'''
		print "[-] String index : %d \n" % self.programCount,
		self.running = True
		self.dbg = pydbg()
		self.dbg.set_callback(EXCEPTION_ACCESS_VIOLATION, self.checkCrash)
		pid = self.dbg.load(self.programPath, self.copyFile+self.ext)
		self.pid = self.dbg.pid
		self.dbg.run()

		if self.pid == None:
			return

	# Fuzz.Monitor debugger
	def monitorDebugger(self):
		'''
		doc : Sleeps for the specified time and terminates the process
		'''
		print "Current Monitoring",
		
		counter = 0
		while counter < self.runTime:
			time.sleep(1)
			print counter,
			counter += 1
		print
		time.sleep(1)

		if self.crashHandler != True:
			time.sleep(1)
			try:
				self.dbg.terminate_process()
			except:
				pass
			self.pid = None
			self.running = False
		else:
			pass
		self.pid = None
		self.running = False

	def checkCrash(self, dbg):
		'''
		doc : When a crash is found, the memory information is extracted,
		the EIP register information is hashed into MD5, and the data is saved,
		a temporary file is created based on various registry information,
		and the crash data author is created after the crash file is created.
		'''
		try:
			os.mkdir("crash")
		except:
			pass
		print "[+] Crash \n",
		self.crashHandler = True
		self.crashBin = utils.crash_binning.crash_binning()
		self.crashBin.record_crash(dbg)
		self.crashData = self.crashBin.crash_synopsis()

		# crashData to pull -> Thread
		with open('crashAllInfo.txt', 'w') as f:
			f.write(self.crashData)

		# print self.crashData
		eipoff = self.crashData.find("EIP")		       # Crash log to find EIP Register
		eaxoff = self.crashData.find("EAX")		       # Crash log to find EAX Register
		eip = self.crashData[eipoff+5:eipoff+13]      


		# esp
		espoff_start = self.crashData.find("ESP")
		espoff_end = self.crashData.find("+00:")
		esp = self.crashData[espoff_start:espoff_end]

		hashdump = hashlib.md5(eip)                    # Hash the eip register to detect duplicate crashes
		hashdump = hashdump.hexdigest()
		
		# message box crash -> thread 
		with open(".hash.log", 'w') as f:
			f.write("EIP = %s\nhash = %s\n" % (eip, hashdump))
		with open(".esp.log", 'w') as f:
			f.write(esp)


		hashDBFd = open('hashDB.txt', 'r')
		hashDBData = hashDBFd.read()
		hashDBFd.close()

		if not bool(re.search(hashdump, hashDBData)):
			try:
				hashFd = open('hashDB.txt', 'a')
				hashFd.write("EIP = %s & hash = %s & programPath = %s & ext = %s \n" %
				              (eip, hashdump, self.programPath, self.ext))
				hashFd.close()
			except:
				print "[-] %s file does not exist." % "hashDB.txt"

			# Save the Mutate log
			crashLogPath = "crash\\crash - %s [ %d ] [%s].txt" % (eip, self.programCount, self.targetfile)
			crashFd = open(crashLogPath, "w")
			crashFd.write("target Prog = %s \n" % self.programPath)
			crashFd.write(self.crashData)
			crashFd.close()

			# Save the Mutate pickle
			mutateDumpPath = "crash\\crash - %s [ %d ] [%s].dump" % (eip, self.programCount, self.targetfile)
			mutateFd = open(mutateDumpPath, "w")
			pickle.dump(self.mutateDic, mutateFd)
			mutateFd.close()

			# Copy the crash file
			crashPath = "crash\\crash - %s [%d] [%s]%s" % (eip, self.programCount, self.targetfile, self.ext)
			shutil.copy(self.copyFile+self.ext, crashPath)
			orignPath = self.sampleFolder + "\\" + self.targetfile

			orignPath = os.getcwd() + "\\" + orignPath
			crashPath = os.getcwd() + "\\" + crashPath
			crashLogPath = os.getcwd() + "\\" + crashLogPath
			mutateDumpPath = os.getcwd() + "\\" + mutateDumpPath
			self.crashData = "target Prog = %s \n %s" % (self.programPath, self.crashData)
			#self.upload(orignPath, crashPath, self.crashData, mutateDumpPath)

		else:
			print "\n[-] same Crash hash : %s " % hashdump
		print "["+ "-"* (len(hashdump)+21) +"]"

		self.crashHandler = False
		self.pid = None

		try:
			self.dbg.terminate_process()
		except:
			pass
		return DBG_EXCEPTION_NOT_HANDLED

# CLI SETTING MAIN
'''
def main():
	parser = optparse.OptionParser("python %prog " + "-t <target Program> -s <sample folder>")
	parser.add_option('-t', '--target', dest='targetProgram', type='string',help='specify target Profram Pull Path')
	parser.add_option('-s', '--sample', dest='sampleFolder', type='string',help='specify sample folder name')
	
	(options, args) = parser.parse_args()
	targetProgram = options.targetProgram
	sampleFolder = options.sampleFolder

	if((targetProgram == None) | (sampleFolder == None)):
		print '[-] You must specify a target file and target Program and file extension'
		print '[-] python filename.py -h '
		exit(0)
	
	print "[*] Binary Fuzzing"
	fuzzer = file_fuzzer(targetProgram, sampleFolder)
	fuzzer.fuzz()
'''
class mainDialog(QDialog, main_.Ui_Dialog):
	'''
	Argv : QDialog : PyQt QDialog class
	Argv1 : main_.UI_Dialog : PyQt UI class
	doc : PyQt UI slot, signal processing
	'''
	def __init__(self):
		'''
		init : 
			setupUi : PyQt ui setting
			programPath : fuzzing binary path
			samplePath : TestCase file path
			step : ProgressBar process
			btn_main_1 -> openProgramPath
			btn_main_2 -> openSamplePath
			btn_main_3 -> enterData
		'''
		QDialog.__init__(self)
		self.setupUi(self)
		self.programPath = ''
		self.samplePath = ''
		self.step = 0
		# mainwindow btn slot
		self.btn_main_1.clicked.connect(self.openProgramPath)
		self.btn_main_2.clicked.connect(self.openSamplePath)
		self.btn_main_3.clicked.connect(self.enterData)

	
    # program path button
	def openProgramPath(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', '*')
		self.programPath = fname 
		self.edit_main_1.setText(fname)

    # sample path button
	def openSamplePath(self):
        # sample path
		fname = QFileDialog.getExistingDirectory(self, 'Open file')
		self.samplePath = fname
		self.edit_main_2.setText(fname)
    
	# opeh hashDB Thread function
	def openCrashFile(self):
		while True:
			try:
				with open('crashAllInfo.txt', 'r') as f:
					self.textBrowser_2.append(f.read())
			except:
				self.textBrowser_2.append("not crash")
				continue
			
			try:
				with open('.esp.log', 'r') as f:
					self.textBrowser.append(f.read())
			except:
				self.textBrowser.append("is input?")
				continue
							
			time.sleep(3) 

			# event 
			if self.step == 10:
				self.showdialog()
			if self.step >= 100:
				print("FIN")
				# message BOx GO?


			self.step += 1
			self.progressBar.setValue(self.step)
			
	# next stacked -> stack thread (0)
	def enterData(self):
		'''
		doc : 2 thread processing
				1. file_fuzzer class instance
				2. openCrashFile
		'''


        # translation sub layout
		print("Loading next Stacked")
        # fuzzing class (file_fuzzer)
	
		fuzzer = file_fuzzer(str(self.programPath), str(self.samplePath))
		self.stacked.setCurrentIndex(1) 		

		nextStackThread = threading.Thread(target=fuzzer.fuzz)
		nextStackThread.setDaemon(1) #True is Program exit together
		nextStackThread.start()	
		
		# textBrowser_2 testing file save to load
		openCrashFileThread = threading.Thread(target=self.openCrashFile)
		openCrashFileThread.setDaemon(0)
		openCrashFileThread.start()		
	
	# messagebox
	def showdialog(self):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)
		msg.setText("CRASH DETECTED")
		msg.setInformativeText("")
		msg.setWindowTitle("CRASH DETECTED")

		try:		
			with open(".hash.log", 'r') as f:
				msg.setDetailedText(f.read())
		except:
			msg.setDetailedText("NOT CRASH")

		# msg.setDetailedText("MD5 %s" % CRASH_HASH)
		msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		msg.buttonClicked.connect(self.msgbtn)
			
		retval = msg.exec_()
		print "value of pressed message box button:", retval
			
	def msgbtn(self):
		print "Button pressed is:"

		
def main():
	app = QApplication(sys.argv)
	dlg = mainDialog()	
	dlg.show()
	app.exec_()
	

if __name__ == '__main__':
	#dbg_thread start
	pydbg_thread = threading.Thread(target=main)
	pydbg_thread.setDaemon(0)
	pydbg_thread.start()
