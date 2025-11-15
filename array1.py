import sys

# Default numbers already included
scores = [10, 20, 30, 40, 50]

if len(sys.argv) > 1:
    scores = [float(n) for n in sys.argv[1:]]
else:
    # If you don’t type anything, these numbers will be used
    print("Using default scores:",scores)
   

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum:", total)
print("Average:", average)
print("Max:", maximum)
print("Min:", minimum)
