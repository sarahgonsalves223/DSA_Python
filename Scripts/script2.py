import os

path = "/Users/sarahgonsalves223/Desktop/DSA_Python/medium/"
files = []
for r, d, f in os.walk(path):
    for fule in f:
        if ".py" in fule and "ac" in fule:
            parts = fule.split(".")
            parts2 = [parts[0], "medium", parts[1]]
            new_name = "_".join(parts2) + ".py"
            print(os.path.join(r, new_name))
            os.rename(os.path.join(r, fule), os.path.join(r, new_name))
