import os


file = open('../Outputs/output.txt', 'r')
lines = file.readlines()
file.close()
with open('output.csv', 'w') as f:
    for line in lines:
        filename = stmts = branch = coverage = ""
        if line.startswith('build'):
            words_list = line.split()
            filename = os.path.basename(words_list[0])
            stmts = words_list[1]
            branch = words_list[3]
            coverage = words_list[5]
            f.write(filename + "," + stmts + "," + branch + "," + coverage+"\n")
    f.close()

