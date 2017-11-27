

#!/usr/bin/python
import sys

with open(sys.argv[1]) as f0:
        # do some stuff.
        human_data=[h.strip().split('\t') for h in f0.readlines()]

with open(sys.argv[2]) as f0:
        # do some stuff.
        mouse_data=[h.strip().split('\t') for h in f0.readlines()]

print "Read", len(human_data), "alignments from", sys.argv[1]
print "Read", len(mouse_data), "alignments from", sys.argv[2]

#human_data.sort()
#mouse_data.sort()
for d in zip(human_data,mouse_data):
    if d[0][0] != d[1][0]:
       
        print(d[0][0])
        print(d[1][1])
        print("*"*42)
mouse_unique = []
mouse_human_hybrid = []
for d in zip(human_data, mouse_data):
    if d[0][0] == d[1][0] and d[0][0][0] != '@':
        if 'chr' in d[1][2] and 'chr' in d[0][2]:
            mouse_human_hybrid.append(d)
        elif 'chr' in d[1][2] and 'chr' not in d[0][2]:
            mouse_unique.append(d[1])
print "unique_mouse=",len(mouse_unique),"mouse_human_hybrid=",len(mouse_human_hybrid)

f = open("mouseunique.sam", "w")

for d in mouse_unique:
    f.write("\t".join(d) + "\n")

f.close()
