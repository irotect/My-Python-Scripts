# sum of multiples of 3 and 5 below 1000
N = 1000
multiples = set()

for x in range(0, N):
    if x % 3 == 0:
        multiples.add(x)
    if x % 5 == 0:
        multiples.add(x)
print(multiples)
print(f"Sum of multiples of 3 or 5 below {N} is {sum(multiples)}")
