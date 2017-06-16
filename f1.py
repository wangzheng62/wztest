from multiprocessing import Process, freeze_support,Queue
import pymssql,time
#查询QQ号

def f(s,tbstart,dbstart,dbend,q):
	conn=pymssql.connect('127.0.0.1','sa','12345678')
	print(conn)
	cr=conn.cursor()
	start=time.time()
	i=1
	j=tbstart
	db=dbstart
	sql=''
	print('查询开始')
	try:
		while(db<=dbend):
			while(i<=100):
				sql=sql+'select * from groupdata%s.dbo.group%s with(index(qqnum_index)) where qqnum=%s union all '%(db,j,s)
				i+=1
				j+=1
			i=1
			db+=1
		sql=sql[:-10]+';'
		cr.execute(sql)
		t=cr.fetchall()
	except Exception as e:
		print(e)
		#pass
	end=time.time()
	print(end-start)
	#print('子程序查询结果：%s'%l)
	q.put(t)
#if __name__=='__main__':
def m(s):
	#global conn1,conn2,conn3,conn4

	q=Queue()
	t=[('ID','QQ号','QQ名','年龄','gender','权限','QQ群号')]
	p1=Process(target=f,args=(s,1,1,3,q,))
	p2=Process(target=f,args=(s,301,4,6,q,))
	p3=Process(target=f,args=(s,601,7,9,q,))
	p4=Process(target=f,args=(s,901,10,11,q,))

	p1.start()
	
	p2.start()

	p3.start()

	p4.start()
	
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	print(t)
	while not q.empty():
		t.append(q.get())
	print('队列信息：%s'%t)
def queryqunnum(s):
	start=time.time()
	l=[('ID','QQ成员','QQ名','年龄','gender','权限等级','QQ群号','群名字')]
	try:
		if isinstance(s,int):
			s=str(s)
		s1=s[:-7]
		s2=s[:-5]
		s3=s[:-6]
		if s1=='':
			s1=0
		s1=int(s1)+1
		s2=int(s2)+1
		if s3=='':
			s3=0
		s3=int(s3)+1
		sql='select * from groupdata%s.dbo.group%s with(index(qunnum_index)) where qunnum=%s'%(s1,s2,s)
		sql01='select qunnum,title from quninfo%s.dbo.qunlist%s where qunnum=%s;'%(s1,s3,s)
		print(sql,sql01)
		'''conn=pymssql.connect('127.0.0.1','sa','12345678')
		cr=conn.cursor()
		qunnum=s
		cr.execute(sql)
		t1=cr.fetchall()'''
		'''cr.execute(sql01)
		t2=cr.fetchone()
		if t1==None:
			pass
		else:
			if t2==None:
				t=[]
				for row in t1:
					row=list(row)
					row.append(None)
					t.append(row)
			else:
				t=[]
				for row in t1:
					row=list(row)
					row.append(t2[1])
					t.append(row)'''
		l[len(l):len(l)]=t1
	except Exception:
		pass
	end=time.time()
	print(end-start)
	print(l)
	return l
if __name__=='__main__':
	
	#m(350388250)
	queryqunnum(53594732)