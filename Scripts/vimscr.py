fule = open("/Users/sarahgonsalves223/Desktop/DSA_Python/problems")
contents = fule.read()
lines = contents.split("\n")
problems = []
for i,line in enumerate(lines):
    if i%2 == 0:
        problems.append(line.strip())
print problems
