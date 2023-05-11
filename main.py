
# read a file as lines
data = open('/home/konqi/repos/itos_exp/itos_exp3/result.txt').readlines()
# filter out empty lines
data = [line.strip() for line in data if line.strip()]
# split each line by ,
data = [line.split(',') for line in data]
# convert each line to a 4-element tuple, where only the first is a string and the rest are integers
data = [(line[0], int(line[1]), int(line[2]), int(line[3])) for line in data]

# group by the first element of each tuple
groups = {}
for line in data:
    if line[0] not in groups:
        groups[line[0]] = []
    groups[line[0]].append(line[1:])

# sort each group by the second element of each tuple
for kind in groups:
    groups[kind].sort(key=lambda x: x[0])

# print the result
print(groups)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5, 3.5), dpi=600)
ax = fig.add_subplot(111)

for kind in ['fifo','lru','opt']:
    ax.plot([x[0] for x in groups[kind]], [x[1] for x in groups[kind]], label=kind)

ax.set_xlabel('Memory Size')
ax.set_ylabel('Hit count')
ax.legend()

fig.savefig('result.png', bbox_inches='tight')
