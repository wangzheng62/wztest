# -*- coding: utf-8 -*-  
# SmallestService.py  
#  
# A sample demonstrating the smallest possible service written in Python.  
  
import win32serviceutil  
import win32service  
import win32event   
import logging  
  
import sys   
import logging  
  
import threading  
import time  
sys.path.append('D:\\qqinfoweb')
from views import app 
logging.basicConfig(level=logging.DEBUG,  
format='%(asctime)s %(levelname)s %(message)s',  
filename=r'log234.txt',  
filemode='a+')  
  
import socket, time  
import random, struct  
import urllib  
  
class SmallestPythonService(win32serviceutil.ServiceFramework):  
	_svc_name_ = "Sologin Monitor Service"  
	_svc_display_name_ = "Sologin Monitor Service"  
  
	def __init__(self, args):  
		self.threads = []  
		logging.error("add thread on port t")  
		win32serviceutil.ServiceFramework.__init__(self, args)  
# Create an event which we will use to wait on.  
# The "service stop" request will set this event.  
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)  
  
	def SvcStop(self):  
# Before we do anything, tell the SCM we are starting the stop process.  
		self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)  
# And set my event.  
  
		win32event.SetEvent(self.hWaitStop)  
  
	def SvcDoRun(self):  
# 把你的程序代码放到这里就OK了
		
		print('hhh')
		self.threads = []  
  
		logging.error("add thread on port ")  
  
		win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)  
  
if __name__=='__main__':  
	win32serviceutil.HandleCommandLine(SmallestPythonService)   
# 括号里的名字可以改成其他的，必须与class名字一致；  