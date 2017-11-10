#
#	python data.ped.py > me.ped
#


f=open("GPS32-228968-9210423.CEL_call_code.txt-datapy")

data=f.readlines()

dna={'A':'1','C':'2','G':'3','T':'4','-':'0'}

begin="HOMOLOG_US\tHOMOLOG_US\t0\t0\t1\t1"
for i in data:
	l=i.split()
	begin+="\t"+dna[l[3][0]]+"\t"+dna[l[3][1]]

print begin
