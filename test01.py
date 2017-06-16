import pymssql
def do():
	func=__listener()
	func.send(None)
	conn=pymssql.connect('127.0.0.1','sa','12345678')
	cr=conn.cursor()
	sql='''
SELECT [__$start_lsn]
      ,[__$end_lsn]
      ,[__$seqval]
      ,[__$operation]
      ,[__$update_mask]
      ,[loginname]
      ,[logintime]
  FROM [manager].[cdc].[dbo.test_CT]
GO'''
	while(True):
		cr.execute(sql)
		t=cr.fetchall()
		if t:
			r=func.send(t)
			print(r)
			break
def __listener():
	r='成功'
	while(True):
		n=yield r
		print(n)
	
if __name__=='__main__':
	do()
		
			
		
	