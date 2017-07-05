'处理客户端'
def server():
	r='接收成功'
	r1='第二步'
	print('初始化')
	n=yield r
	#第一步
	print('第一步')
	if n:
		print('接收的信息是：%s'%n)
	n=yield r1
	#第二步
	if n:
		print('接收的信息是：%s'%n)
	n=yield r1