import math
for z in range(int(raw_input())):
	n=int(raw_input())
	l=map(int,raw_input().split())
	print int(math.ceil(float(n)/3.0)),int(math.ceil(float(n)/2.0))
