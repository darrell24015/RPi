import sys
k = "Hello"
y = "World"
# the next line doesn't work, why? Is it because Python3 vs 2?
# version = sys.version_info(0)
print(k + " " + y)
print("We are running Python " + sys.version)
