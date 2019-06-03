
import urllib.request
class Element():
	def __init__(self,**kw):
		self.level=kw['level']
		self.tag=kw['tag']
		self.attributes=kw['attributes']
		self.innerhtml=kw['innerhtml']
		self.father=kw['father']
#-----------------------------
class Page():
	def __init__(self,url):
		self.url=url
	def gethtml(self):
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
		req = urllib.request.Request(url=self.url, headers=headers)
		content=urllib.request.urlopen(req).read().decode('gbk')
		res=[]
		l=[]
		n=0
		switch=False
		while(n<len(content)):
			c=content[n]
			if switch:
				if c=='>':
					l.append(c)
					tmp="".join(l)
					res.append(tmp)
					l=[]
					switch=False
				else:
					l.append(c)
			else:
				if c=='<':
					tmp="".join(l)
					l=[]
					res.append(tmp)
					switch=True
					l.append(c)
				else:
					l.append(c)
			n=n+1
		res.pop(0)
		return res
	def istag(self,s):
		s=s.replace('<','')
		s=s.replace('>','')
		s=s.strip()
		res={'tag':'',
		'type':1,
		'attributes':{},
		'innerhtml':[]}
		l=s.split(' ')
		print(l)
		if l[0][0]=='/':
			res['type']=-1
		elif l[-1][0]=='/':
			res['type']=0
		else:
			res['type']=1
			if len(l)>1:
				for index,f in enumerate(l):
					if index!=0 and '=' in f:
						tmpl=f.split('=',1)
						res['attributes'][tmpl[0]]=tmpl[1]
		t=l[0].replace('/','')
		res['tag']=t
		return res
	#顺序读取整个html列表
	#level是元素的深度，index是父元素的innerhtml列表长度-1
	#当tag类型为1时为tag开始标志，创建新元素，如果上个tag的type是1，则代表tag为上个元素的子元素，level加1，如果上个tag的type是-1则代表tag是上个元素的同级元素，level不变
	#当tag类型为-1时为tag封闭标志，如果上个tag的type是1，则代表上个tag封闭，level不变，如果上个tag是type则代表上个tag的父元素封闭，level减1
	#当tag类型是0时，创建新元素，level不变
	def getelement(self):
		level=0
		father=0
		now=0
		for s in self.gethtml():
			if s!='':
				#<tag>
				if s[0]=='<' and s[-1]=='>':
					#排除注释
					if s[1]=='!':
						pass
					#	
					else:
						tag=self.istag(s)
						print(tag)
						if tag['type']==0:
						#一个新element
						elif tag['type']==1:
							level=level+tag['type']
							tag['father']=father
							e=Element(tag)
							father=e
						elif tag['type']==-1:
							
						else:
							pass
				#
				else:
def getelementbyID(id,l):
	condition='id="{}"'.format(id)
	tagstack=[]
	content=[]
	switch=False
	n=0
	while(n<len(l)):
		c=l[n]
		if switch:
			if len(c)>1:
				if c[0]=='<' and c[1]!='/' and c[-1]=='>' and c[-2]!='/':
					tagstack.append(c)
				elif c[0]=='<' and c[1]=='/':
					tagstack.pop()
					if len(tagstack)==0:
						content.append(c)
						break
			content.append(c)								
		else:
			if condition in c:
				switch=True
				tagstack.append(c)
				content.append(c)
		n=n+1
	res=content
	#print(tagstack)
	return res
	#res=['<div>','</div>']
			
	

if __name__=='__main__':
	url=r"https://www.banzhu01.org/4_4370/405192.html"
	p1=Page(url)
	p1.getelement()