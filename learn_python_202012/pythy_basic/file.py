import os

fo = open(os.path.dirname(__file__) +
          "/datamappingConfig_example_32E2", "r")
print(fo.name)

raw_contents = fo.readlines()
for line in raw_contents:
    if line.split(" ")[0] == "refrencePointB":
        print(line)

for i in range(1, 54):
    fo.readline()
    i += 1
    if i == 46:
        referenceB = fo.readline()
        print(referenceB)

fo.close

print("m:")
for m in range(1, 4):
    for n in range(4, 6):
        print(m, n)
