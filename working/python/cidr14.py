#!/usr/bin/env python3

net14 = []
for i in range(0, 256, 4):
	net14.append(i)

for h in net14:
	print("{0},{1},{2}".format("Network Block", "Class B", "Location"))
	print("10." + str(h) + ".0.0/14,")
	a = h + 1
	b = h + 2
	c = h + 3

	print("    ,10."+ str(h) + ".0.0/16")
	print("    ,10."+ str(a) + ".0.0/16")
	print("    ,10."+ str(b) + ".0.0/16")
	print("    ,10."+ str(c) + ".0.0/16")

