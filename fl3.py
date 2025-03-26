op=open('newfile1.txt','w')
ip=open('n.txt','r')

lines=set()
print("remove the duplicate lines..")


for line in ip:
    if line not in lines:
        op.write(line)
        lines.add(line)
ip.close()
op.close()        