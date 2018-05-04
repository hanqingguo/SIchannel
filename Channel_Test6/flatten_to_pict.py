import cv2
import numpy as np

f = open('receive_out2','r')
lines = f.readlines()
print(type(lines))
flattened = []
for line in lines:
	print(line)
	flattened.append(int(line[:-1]))
flt = np.array(flattened)
print(flt.shape)
new = flt.reshape(128,128,3)
print(new)
print(type(new))
cv2.imwrite('receive.png', new)
	
