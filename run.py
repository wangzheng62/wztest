db=10
dbend=11
sql=''
i=1
j=(db-1)*100+1
s=123445
while(db<=dbend):
	while(i<=100):
		sql=sql+'select qqnum,nick,age,gender,auth,qunnum from groupdata%s.dbo.group%s with(index(qqnum_index)) union all '%(db,j)
		i+=1
		j+=1
	i=1
	db+=1
sql=sql[:-10]+';'
print(sql)		
		
		

