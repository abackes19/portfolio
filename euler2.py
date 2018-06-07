# this function will return the desired output of the fibonacci sequence, given the term
def fib(n):
    if n == 1:
        return n
    elif n == 2:
        return n
    elif n > 2:
# This line will take the previous and second previous terms and run
# them through the fib function as well
# and it will all loop back until n = 1 (the start)
        return fib(n-2) + fib(n-1)

n = 1
output = 1
total = 0

# This while loop will loop through, adding and finding the next
# even fibonacci number, until it exceeds the value of 4 million
while output < 4000000:
# This will find the fibonacci term using the fib function, and set it equal to the output
    output = fib(n)
# this ensures that only even numbers that are less than 4 million will be added
    if output % 2 == 0 and output < 4000000:
        total = total + output
# adds one to the term, repeats the process with the next fibonacci number
    n = n + 1

print "The Grand Total: %d" % total
