# del print
array = ['pink','yellow','green']
del array[1]
print array

# as for in import print
import calendar as c

for i in range(1,13):
	print c.month_name[i]

# global print
var = 0
def globaltest():
	global var
	var = var + 25
	print var

globaltest()
globaltest()
var += var
print var
globaltest()

# with as open close write """
with open("output.txt","w") as out:
	lines = """The central principle of the 
Babbel language learning approach is that people 
should spend about 15 minutes per day 
studying a new language. This is 
surprisingly short compared to the 
length of time university students are expected to study a language nightly (~90 minutes). 
"""

	out.write(lines)
	out.close()

# assert  try except logging finally pass raise
import logging

def throw(msg):
	x = msg

# if condition returns False, AssertionError is raised:
	try:
		assert x == "goodbye", "x is 'hello'"
	except AssertionError:
		logging.error("Assert error",exc_info=True)
		raise ValueError("goodbye",msg)
	finally:
		pass

try:
	throw('Hello')
except ValueError:
	logging.error("Value error",exc_info=True)
finally:
	pass

# pass

def hello():
	pass

class Make:
	pass

print "Calling hello."
hello()

print "Printing class Make"
print Make

# yield def while 
def fibonacci(n):
    curr = 1
    prev = 0
    counter = 0
    while counter < n:
        yield curr
        prev, curr = curr,prev+curr
	counter += 1


for i in fibonacci(25):
	print i,
	print " ",
print

# range break continue
for i in range(9):
	print(i)
	if i > 3:
    		break

for i in range(9):
	print(i)
  	if i > 3:
    		continue

# exec
prog = 'print "The sum of 5 and 10 is", 5+10'
exec(prog) 	

# lambda
fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)

def fibseq(n):
	for i in range(n):
		print fib(i),
		print " ",

fibseq(20)

# None 
variable = None
print type(variable)
if variable:
	print True
else:
	print False
