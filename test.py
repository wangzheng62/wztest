class Dt(dict):
	def __init__(self,**kw):
		super(Dt,self).__init__(**kw)
if __name__=='__main__':
	d={'username':'test','pw':'123'}
	dt=Dt(**d)
	print(dt.keys())
	print(dir(dt))
	for k in dt:
		print(k)
	
			
		
	