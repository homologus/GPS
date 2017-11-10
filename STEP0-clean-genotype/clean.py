#
#
#	This script keeps the lines from
#	genotype file that are present in PAP.bim
#
#	To run, 
#	(i) copy GPS32-228968-9210423.CEL_call_code.txt.gz from my-genotype-dat
#	folder and uncompress the file
#	(ii) run 'python clean.py > GPS32-228968-9210423.CEL_call_code.txt-datapy'
#



f=open("PAP.bim")
data=f.readlines()
exist={}
for i in data:
	i=i.strip()
	l=i.split()
	exist[l[1]]=1



f=open("GPS32-228968-9210423.CEL_call_code.txt")
data=f.readlines()

for i in data:
	i=i.strip()
	l=i.split()
	if l[0] in exist:
		print i
