# A Python program to print all
# permutations using library function
from itertools import permutations

name=[]
fname=['123','0','1','2','3','1234','@','#','$','%','&','_','-']
while True:
    iname=input("enter the name").lower()
    if iname=='n':
        print (iname)
        break
    name.append(iname)
    name.append(iname.title())
    name.append(iname.upper())

for i in name:
    if i not in fname:
        fname.append(i)

print(fname)

flist=['Monika','Pradeep', 'Sonika', 'Aashi','Myra','Geeta','Singh','1981','2006','1985','%','@','$']
# Get all permutations of [1, 2, 3]
num=0
for choice in range(1,4):
    perm = permutations(fname,choice)


    f = open('file11.txt','w')
    # Print the obtained permutations
    for i in list(perm):
        # print (i)
        res = ''.join(i)
        f.write(res+'\n')
        # print (str(res))
        num+=1
f.close()
print(num)
