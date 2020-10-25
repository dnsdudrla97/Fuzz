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

class file_fuzzer:
	def __init__(self, targetProgram, sampleFolder):
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
		self.crashData = None
		self.badChar = ["\x00", "\x41", "\xff", "\x0c", "\xAA"]
		self.badVector = [[os.urandom(4), os.urandom(4), os.urandom(4), os.urandom(4), os.urandom(4), "\x00\x00\x00\x00", "\xff\xff\xff\xff", ],
                     ["A"*5, "A"*17, "A"*33, "A"*65, "A"*129, "A"*257, "A" *513, "A"*1024, "A"*2049, "A"*4097, "A"*8193, "A"*12288, ],
                     ["%99n", "%s%p%x%d", ".1024d", "%.2049d", "%n%n", "%p%p", "%x%x", "%d%d", "%s%s", "%99999999999s", "%08x", "%%20d",
                     	"%%20n", "%%20x", "%%20s", "%#0123456x%08x%x%s%p%d%n%o%u%c%h%l%q%j%z%Z%t%i%e%g%f%a%C%S%08x%%", "%s"*129, "%x"*257, ],
                     ["\x3f\xff", "\xff\x3f", "\x7f\xff", "\xff\x7f","\x80\x00", "\x00\x80", "\xfe\xff", "\xff\xfe", ],
                     ["\x00\x00\x01\x00", "\x00\x01\x00\x00", "\x00\x00\x10\x00", "\x00\x01\x00\x00", "\x00\x00\x01\x00", "\x00\x10\x00\x00", "\x3f\xff\xff\xff", "\xff\xff\xff\x3f", "\x7f\xff\xff\xfe", "\xfe\xff\xff\x7f", "\x7f\xff\xff\xff", "\xff\xff\xff\x7f", "\x80\x00\x00\x00", "\x00\x00\x00\x80", "\xff\xff\xff\xfe", "\xfe\xff\xff\xff", ]]

	def fuzz(self):
		while 1:
			if not self.running:
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
				self.mutationFile()											   # Mutate Target file

				try:
					self.dbg.terminate_process()
				except:
					pass

				#dbg_thread start
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

				#monitor_thread start
				monitor_thread = threading.Thread(target=self.monitorDebugger)
				monitor_thread.setDaemon(0)
				monitor_thread.start()
			else:
				time.sleep(1)

	# Fuzz.Mutate Target file
	def mutationFile(self):
		self.mutateDic = {}									                            # Reset Mutate key

		try:
			copyFd = open(self.copyFile+self.ext, "w+b")	                            # Copy File Open(w+b)
			copyFd.write(self.stream)						                            # Save the File Stream
			print "[-] Mutate %s" % self.targetfile,		               	            # Print Target File Name
		except:
			print "[-] File Copy Failed"
			return

		# The mutate counter is based on the Full length 
		streamLength = len(self.stream)					                                # Get the Full length of the target file
		mutateCount = int(streamLength*0.01)
		mutateCount2 = int(streamLength*0.0001)
		print "Count : %d and Count2 : %d" % (mutateCount, mutateCount2)	            # Print Mutate Count

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
			print "randVector : %s" % randVector
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
		# Sleeps for the specified time and terminates the process
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
		try:
			os.mkdir("crash")
		except:
			pass
		print "[+] Crash \n",
		self.crashHandler = True
		self.crashBin = utils.crash_binning.crash_binning()
		self.crashBin.record_crash(dbg)
		self.crashData = self.crashBin.crash_synopsis()

		print self.crashData
		eipoff = self.crashData.find("EIP")		       # Crash log to find EIP Register
		eaxoff = self.crashData.find("EAX")		       # Crash log to find EAX Register
		eip = self.crashData[eipoff+5:eipoff+13]      

		hashdump = hashlib.md5(eip)                    # Hash the eip register to detect duplicate crashes
		hashdump = hashdump.hexdigest()

		print "["+ "-"* (len(hashdump)+6) +"]"
		print "EIP = %s\nhash = %s\n" % (eip, hashdump),
		print "["+ "-"* (len(hashdump)+6) +"]"

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


if __name__ == '__main__':
	main()
