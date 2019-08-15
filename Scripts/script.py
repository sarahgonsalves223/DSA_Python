import subprocess
from subprocess import Popen, PIPE
import os

file_p = open("/Users/sarahgonsalves223/Desktop/DSA_Python/problems", "r")
contents = file_p.read()
lines = contents.split("\n")
problems = []
for i,line in enumerate(lines):
    if i%2 == 0:
        problem = line.strip()
        problems.append(problem)
        command = "leetcode submission " + problem + " -x"
        try:
            output = subprocess.check_output(command.split(" "))
            print(output)
        except Exception as ex:
            print(ex)
            print("exception caught!")

