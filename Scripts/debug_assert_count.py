import collections
import os
import re

import matplotlib.pyplot as plt

asserts_dict = {}
debugs_dict = {}
for root, dirs, files in os.walk('C:/Usha/Courses/PAT/finalproject/numpynew/numpy/numpy'):
    for filename in files:
        if re.match('^((?!test).)*.py$', filename) and not (root.__contains__("test")):
            filepath = os.path.join(root, filename)
            # print(filepath, end='')
            with open(filepath, "r", encoding='utf-8') as file:
                file_data = file.read()
                file.close()
                assert_stmts = file_data.count("assert")
                # print(assert_stmts)
                if asserts_dict.get(assert_stmts):
                    asserts_dict.get(assert_stmts).append(filename)
                else:
                    asserts_dict[assert_stmts] = [filename]
                debug_stmts = file_data.count("debut")
                #print("\t",debug_stmts)
                if debugs_dict.get(debug_stmts):
                    debugs_dict.get(debug_stmts).append(filename)
                else:
                    debugs_dict[debug_stmts] = [filename]

odict_asserts = collections.OrderedDict(sorted(asserts_dict.items(), reverse=True))
odict_debugs = collections.OrderedDict(sorted(debugs_dict.items(), reverse=True))

index = 10
assertsfilenamesList = []
numberofassertslist = []
for key, value in odict_asserts.items():
    if index > 0:
        for i in range(len(value)):
            assertsfilenamesList.append(value[i])
            numberofassertslist.append(key)
        index -= 1

debugsfilenamesList = []
numberofdebugslist = []
for key, value in odict_debugs.items():
    for i in range(20):
        debugsfilenamesList.append(value[i])
        numberofdebugslist.append(key)

figure, axis = plt.subplots(2)

axis[0].plot(assertsfilenamesList, numberofassertslist, color="green")
axis[0].tick_params(labelrotation=30)
axis[1].plot(debugsfilenamesList, numberofdebugslist, color="red")

# naming the x axis
#axis[0].xlabel('prod. file names with top assert stmts.')
# naming the y axis
#axis[0, 0].ylabel('Nr. of assert stmts.')

# giving a title to my graph
plt.title('Assert and Debug stmts. graph')
plt.xticks(rotation=30, ha="right")




# naming the x axis
#axis[1, 0].xlabel('prod. file names with top debug stmts.')
# naming the y axis
#axis[1, 0].ylabel('Nr. of debug stmts.')


# function to show the plot
plt.show()
