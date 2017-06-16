import pymssql
def __listener():
	r=''
	while(True):
		n=yield r
		while(n):
			print('数据库需要重新连接')
			n=None
			f()
def f():
	SEVERCONFIG=['127.0.0.1','sa','12345678']
	try:
		conn=pymssql.connect(*SEVERCONFIG)
		print(conn)
	except Exception as e:
		c=__listener()
		c.send(None)
		c.send(e)
if __name__=='__main__':
	f()
			