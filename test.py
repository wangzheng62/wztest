import pymssql,mysql.connector
def mssql():
	conn=pymssql.connect('127.0.0.1','sa','12345678')
	cr=conn.cursor()
	cr.execute('create database test;')
	conn.commit()
def my():
	conn=mysql.connector.connect(host='127.0.0.1',user='root',password='12345678')
	cr=conn.cursor()
	cr.execute('create database test;')
	conn.commit()
if __name__=='__main__':
	mssql()
		
	