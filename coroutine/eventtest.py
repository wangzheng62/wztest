'事件驱动'
def check():
	name=(yield)
	if name=='test':
		yield True
	else:
		yield False
def login(name,c):
	c.send(None)
	res=c.send(name)
	print(res)
if __name__=='__main__':
	login('test',check())
	login('test1',check())
	