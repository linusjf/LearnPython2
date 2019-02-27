from sys import argv

def  numlist(start,end,inc):
	i = start
	numbers = [] 
	while i < end:
		numbers.append(i)
		if inc <  0:
			i -= inc
		else:
			i += inc
	return numbers

end = int(argv[1])
inc = int(argv[2])

print "The numbers: "
numbers = range(0,end,inc)
for num in numbers:
	print num 
