#
# python data.map.py > me.map
#


f=open("GPS32-228968-9210423.CEL_call_code.txt-datapy")

data=f.readlines()

dna={'A':'1','C':'2','G':'3','T':'4','-':'0'}

for i in data:
	l=i.split()
	print l[1]+"\t"+l[0]+"\t0\t"+l[2]

