import collections
import os
from collections import OrderedDict
import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
from pydriller import Repository

def asserts_plot():
    index = 30
    filenamesList = []
    numberofassertslist = []
    with open("../Outputs/asserts_count.csv", "r", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if index > 1:
                lines_list = line.split(",")
                filenamesList.append(lines_list[0])
                numberofassertslist.append(lines_list[1])
                index -= 1
    file.close()
    plt.plot(filenamesList, numberofassertslist)
    plt.xlabel('file names with top assert stmts.')
    plt.ylabel('Nr. of assert stmts.')

    # giving a title to my graph
    plt.title('Assert stmts. graph')
    plt.xticks(rotation=45, ha="right")

    # function to show the plot
    plt.show()




def debug_assert_plot():
    index = 30
    filenamesList = []
    numberofassertslist = []
    with open("../Outputs/asserts_debug_count1.csv", "r", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if index > 1:
                lines_list = line.split(",")
                filenamesList.append(lines_list[0])
                numberofassertslist.append(lines_list[1])
                index -= 1
    file.close()
    plt.plot(filenamesList, numberofassertslist)
    plt.xlabel('file names with top assert statements')
    plt.ylabel('Nr. of Assert stmts.')

    # giving a title to my graph
    plt.title('Assert Debug statements graph')
    plt.xticks(rotation=45, ha="right")
    plt.show()





def debug_assert_plot2():
    index = 30
    filenamesList = []
    numberofassertslist = []
    with open("../Outputs/asserts_debug_count2.csv", "r", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if index > 1:
                lines_list = line.split(",")
                filenamesList.append(lines_list[0])
                numberofassertslist.append(lines_list[1])
                index -= 1
    file.close()
    plt.plot(filenamesList, numberofassertslist)
    plt.xlabel('file names with top debug statements')
    plt.ylabel('Nr. of Debug stmts.')

    # giving a title to my graph
    plt.title('Assert Debug statements graph')
    plt.xticks(rotation=45, ha="right")

    # function to show the plot
    plt.show()



def branch_coverage():
    file = open('../Outputs/output.csv', 'r')
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

def statement_coverage():
    file = open('../Outputs/output.csv', 'r')
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

    plt.plot(list(stats_dict.keys())[:20], list(stats_dict.values())[:20])
    plt.xlabel('file names')
    plt.ylabel('Nr. of stmts. covered')

    plt.title('Statement Coverage')
    plt.xticks(rotation=45, ha="right")

    plt.show()

def total_coverage():
    file = open('../Outputs/output.csv', 'r')
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

    plt.plot(list(coverage_dict.keys())[:20], list(coverage_dict.values())[:20])
    plt.xlabel('file names')
    plt.ylabel('Coverage Percentile')

    plt.title('Coverage')
    plt.xticks(rotation=45, ha="right")

    plt.show()
month_dict = {}

def add_commits(month,commit):
    if commit.committer_date.date().month == month:
        if month_dict.get(month):
            month_dict[month] += 1
        else:
            month_dict[month] = 1
def commits_by_month():
    start_date = datetime.datetime.now()
    delta_period = 12
    end_date = start_date - relativedelta(months=delta_period) - timedelta(days=-delta_period)

    for commit in Repository('C:/Usha/Courses/PAT/finalproject/numpynew/numpy', since=end_date, to=start_date).traverse_commits():
        # print(len(commit.modified_files))
        add_commits(1, commit)
        add_commits(2, commit)
        add_commits(3, commit)
        add_commits(4, commit)
        add_commits(5, commit)
        add_commits(6, commit)
        add_commits(7, commit)
        add_commits(8, commit)
        add_commits(9, commit)
        add_commits(10, commit)
        add_commits(11, commit)
        add_commits(12, commit)

    # for key,value in month_dict.items():
    #     print(key, value)

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(month_dict.keys(), month_dict.values(), color='green',
            width=0.4)

    plt.xlabel("Month")
    plt.ylabel("Total number of commits")
    plt.title("Number of commits by month")
    plt.show()

def top_contributors():
    start_date = datetime.datetime.now()
    delta_period = 12
    end_date = start_date - relativedelta(months=delta_period) - timedelta(days=-delta_period)
    month_dict = {}
    total_commits = 0
    for commit in Repository('C:/Usha/Courses/PAT/finalproject/numpynew/numpy', since=end_date, to=start_date).traverse_commits():
        # print(len(commit.modified_files))
        total_commits += 1
        author_name = commit.author.name
        if month_dict.get(author_name):
            month_dict[author_name] += 1
        else:
            month_dict[author_name] = 1

    print(total_commits)
    odict = dict(sorted(month_dict.items(), key=lambda item: item[1], reverse=True))
    fig = plt.figure(figsize=(10, 7))
    plt.pie(list(odict.values())[:10], labels=list(odict.keys())[:10])

    # show plot
    plt.show()
asserts_plot()
debug_assert_plot()
debug_assert_plot2()
branch_coverage()
statement_coverage()
total_coverage()
commits_by_month()
top_contributors()