import mysql.connector

class Mysqlservermetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['server']=name
		print('cls:%s,name:%s,bases:%s,attrs:%s'%(cls, name, bases, attrs))
		return type.__new__(cls, name, bases, attrs)
class MysqlserverBase(metaclass=Mysqlservermetaclass):
    pass

# 数据库
class MysqlDbmetaclass(Mysqlservermetaclass):
	def __new__(cls, name, bases, attrs):
		attrs['db']= name
		print('cls:%s,name:%s,bases:%s,attrs:%s'%(cls, name, bases, attrs))
		return type.__new__(cls, name, bases, attrs)
class MysqlDbBase(metaclass=MysqlDbmetaclass):
    pass
	
class Localhost(MysqlserverBase):
	pass
class Test(MysqlDbBase,Localhost):
	pass
	
if __name__=='__main__':
	print(Localhost.server)
	print(Test.server)
	print(Test.db)