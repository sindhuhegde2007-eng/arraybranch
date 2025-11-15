import sys

if len(sys.argv) > 1:
    scores = [float(n) for n in sys.argv[1:]]
else:
    scores = [float(n) for n in input("Enter scores: ").split()]
total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum:", total)
print("Average:", average)
print("Max:", maximum)
print("Min:", minimum)
