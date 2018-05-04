f = open('receive1','r')
f1 = open('receive_out2','w')
lines = f.readlines()
print(len(lines[1]))
for line in lines:
	if(len(line)>4):
		if(len(line)==7):
			f1.write(line[0:3]+'\n')
			f1.write(line[3:])
		elif(int(line[0])<3):
			f1.write(line[0:3]+'\n')
			f1.write(line[3:])
		else:
			f1.write(line[0:2]+'\n')
			if(int(line[2])>2 and len(line)>5):
				f1.write(line[2:4]+'\n')
				f1.write(line[4:])	
			else:	
				f1.write(line[2:])
	elif(line=='\n'):
		f1.write('0'+line)	
	else:
		f1.write(line)
f1.close()
f.close()
