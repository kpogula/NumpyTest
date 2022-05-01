import os
from collections import OrderedDict
import matplotlib.pyplot as plt

file = open('output.csv', 'r')
lines = file.readlines()
file.close()

stats_dict = OrderedDict()
branch_dict = OrderedDict()
coverage_dict = OrderedDict()
for line in lines:
    words_list = line.split(',')
    filename = os.path.basename(words_list[0])
    stmts = words_list[1]
    branch = words_list[2]
    coverage = words_list[3]
    stats_dict[filename] = stmts
    branch_dict[filename] = branch
    coverage_dict[filename] = coverage

plt.plot(list(branch_dict.keys())[:20], list(branch_dict.values())[:20])
plt.xlabel('file names')
plt.ylabel('Nr. of branches covered')

plt.title('Branch Coverage')
plt.xticks(rotation=45, ha="right")

plt.show()