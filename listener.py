def __listener():
	r='结果'
	while(True):
		n=yield r
		if n==4:
			print(n)
#调用监听
def f():
	func=__listener()
	func.send(None)
	while(True):
		n=input('输入一个数字：')
		n=int(n)
		func.send(n)
if __name__=='__main__':
	f()