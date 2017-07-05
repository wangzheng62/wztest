'客户端'
import sys
sys.path.append('D:\\gitworkspace\\wztest\\coroutine')
from server import server
def l(g):
	yield from g
	
def client(msg):
	c=server()
	r=c.send(None)
	r1=c.send(msg)
	print('r:%s'%r)
	#c.send(msg)
	print('r1:%s'%r1)
	c.send(msg)

if __name__=='__main__':
	c=server()
	for i in c:
		print(c)
	
	