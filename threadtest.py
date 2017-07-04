from threading import Thread
import os,time

# 子进程要执行的代码
def run_proc(name):
	i=0
	while(i<100000000):
		i+=1
	print('Run child Thread %s (%s)...' % (name, os.getpid()))
if __name__=='__main__':
	print('Parent Thread %s.' % os.getpid())
	p1 = Thread(target=run_proc,args=('p1',))
	p2 = Thread(target=run_proc,args=('p2',))
	p3 = Thread(target=run_proc,args=('p3',))
	start=time.time()
	print('Child Thread will start.')
	p1.start()
	p2.start()
	p3.start()
	p1.join()
	p2.join()
	p3.join()
	print('Child Thread end.')
	end=time.time()
	print(end-start)