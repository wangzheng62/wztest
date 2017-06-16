from multiprocessing import Process, freeze_support,Queue
import time
start=time.time()
def f(MAX,q):
	s='12345'
	j=0
	while(j<MAX):
		i=int(s)
		s=str(i)
		i=int(s)
		s=str(i)
		i=int(s)
		s=str(i)
		j+=1
	q.put(j)
	print('done')
if __name__=='__main__':
	#f(1000000)
	q=Queue()
	t=[]
	p1=Process(target=f,args=(250000,q,))
	p2=Process(target=f,args=(250000,q,))
	p3=Process(target=f,args=(250000,q,))
	p4=Process(target=f,args=(250000,q,))
	p1.start()
	p2.start()
	p3.start()
	p4.start()
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	while not q.empty():
		t.append(q.get())
	print('队列信息：%s'%t)
	end=time.time()
	print(end-start)
	