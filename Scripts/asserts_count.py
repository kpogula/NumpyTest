import collections
import glob
import os

import matplotlib.pyplot as plt

python_files = glob.glob("numpy/numpy/" + r"/**/*test*.py", recursive=True)

print(len(python_files))
dict = {}

for filepath in python_files:
    # print(filepath, end='')
    with open(filepath, "r", encoding='utf-8') as file:
        file_data = file.read()
        file.close()
        assert_stmts = file_data.count("assert")
        filename = os.path.basename(filepath)
        if dict.get(assert_stmts):
            dict.get(assert_stmts).append(filename)
        else:
            dict[assert_stmts] = [filename]
        # print(",", assert_stmts)

odict = collections.OrderedDict(sorted(dict.items(), reverse=True))
# print(odict)

index = 30
filenamesList = []
numberofassertslist = []
for key, value in odict.items():
    if index > 0:
        for i in range(len(value)):
            filenamesList.append(value[i])
            numberofassertslist.append(key)
        index -= 1

#print(filenamesList)
#print(numberofassertslist)
plt.plot(filenamesList, numberofassertslist)
# naming the x axis
plt.xlabel('file names with top assert stmts.')
# naming the y axis
plt.ylabel('Nr. of assert stmts.')

# giving a title to my graph
plt.title('Assert stmts. graph')
plt.xticks(rotation=45, ha="right")

# function to show the plot
plt.show()