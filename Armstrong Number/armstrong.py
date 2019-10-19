import random

x = random.randint(0,10000)

s = 0

m = x

while x>0:
	y = x%10
	s += y**3
	x = x//10
    
if s == m:
	print ("It is an armstrong no")
else:
	print ("It is not an armstrong no")
