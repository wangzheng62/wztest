from multiprocessing import Process,Queue
import os,time

# 子进程要执行的代码
def run_proc(name,q):
	i=0
	q.put(name)
	while(i<100000000):
		i+=1
	print('Run child process %s (%s)...' % (name, os.getpid()))
if __name__=='__main__':
	q=Queue()
	print('Parent process %s.' % os.getpid())
	p1 = Process(target=run_proc,args=('p1',q))
	p2 = Process(target=run_proc,args=('p2',q))
	p3 = Process(target=run_proc,args=('p3',q))
	start=time.time()
	print('Child process will start.')
	p1.start()
	p2.start()
	p3.start()
	p1.join()
	p2.join()
	p3.join()
	print('Child process end.')
	print(q.qsize())
	print(q.get())
	print(q.get())
	print(q.get())
	print(q.get())
	end=time.time()
	print(end-start)