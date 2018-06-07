# determines if a number is prime by seeing if it is divisable by any
# previously found primes, discounting 2
def prevprime(n):
    for l in primes:
        if n % l == 0:
            return False

total = 2
primes = []

# goes through every odd number under 2 million and tests if its prime
for i in xrange(3, 2000000, 2):
    if prevprime(i) != False:
        primes.append(i)

# this goes through each prime found and adds it to the total
for i in primes:
        total = total + i

print "Total: ", total



# Total:  142913828922
