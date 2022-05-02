import datetime
import os
import re
from collections import OrderedDict
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
    plt.xlabel('File names with top assert statements')
    plt.ylabel('Number of assert statements')

    # giving a title to my graph
    plt.title('Assert Statements Graph')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    # function to show the plot
    plt.show()


def debug_assert_plot():
    index = 15
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
    # plt.plot(filenamesList, numberofassertslist)
    # plt.xlabel('File names with top assert statements')
    # plt.ylabel('Number of Assert statements')
    #
    # # giving a title to my graph
    # plt.title('Assert Debug statements graph')
    # plt.xticks(rotation=45, ha="right")
    # plt.tight_layout()
    # plt.show()

    plt.bar(filenamesList, numberofassertslist, color='orange',
            width=0.4)

    plt.xlabel("File names with top assert statements")
    plt.ylabel("Number of Assert statements")
    plt.title("Assert Statements Plot")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
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
    plt.xlabel('File Names with top debug statements')
    plt.ylabel('Nr. of Debug statements')

    # giving a title to my graph
    plt.title('Debug Statements Graph')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
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
    plt.xlabel('File Names')
    plt.ylabel('Number of branches covered')
    plt.title('Branch Coverage')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
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
    plt.xlabel('File Names')
    plt.ylabel('Number of statements covered')

    plt.title('Statement Coverage')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
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
    plt.xlabel('File Names')
    plt.ylabel('Coverage Percentile')
    plt.title('Coverage')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


month_dict = {}


def add_commits(month, commit):
    if commit.committer_date.date().month == month:
        if month_dict.get(month):
            month_dict[month] += 1
        else:
            month_dict[month] = 1


def commits_by_month():
    start_date = datetime.datetime.now()
    delta_period = 12
    end_date = start_date - relativedelta(months=delta_period) - timedelta(days=-delta_period)

    for commit in Repository('https://github.com/numpy/numpy.git', since=end_date, to=start_date).traverse_commits():
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

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(month_dict.keys(), month_dict.values(), color='green',
            width=0.4)

    plt.xlabel("Month")
    plt.ylabel("Total number of commits")
    plt.title("Number of commits by month")
    plt.tight_layout()
    plt.show()


def top_contributors():
    start_date = datetime.datetime.now()
    delta_period = 12
    end_date = start_date - relativedelta(months=delta_period) - timedelta(days=-delta_period)
    month_dict = {}
    total_commits = 0
    for commit in Repository('https://github.com/numpy/numpy.git', since=end_date, to=start_date).traverse_commits():
        total_commits += 1
        author_name = commit.author.name
        if month_dict.get(author_name):
            month_dict[author_name] += 1
        else:
            month_dict[author_name] = 1

    odict = dict(sorted(month_dict.items(), key=lambda item: item[1], reverse=True))
    fig = plt.figure(figsize=(10, 7))
    plt.pie(list(odict.values())[:10], labels=list(odict.keys())[:10])
    plt.title("Top Contributors Over The Last Year")
    # show plot
    plt.show()


def total_modified():
    files_list = []
    modified_list = []
    file = open('../Outputs/FilesModified.csv', 'r')
    lines = file.readlines()[1:]
    file.close()
    index = 10
    for line in lines:
        if index > 1:
            list_modified = line.split(",")
            files_list.append(list_modified[0])
            modified_list.append(list_modified[1])
            index -= 1

    plt.plot(files_list, modified_list)
    plt.xlabel('File Name')
    plt.ylabel('Number of times file is modified')
    plt.title('Files Modified Plot')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def files_added_by_date():
    start_date = datetime.datetime.now()
    delta_period = 6
    end_date = start_date - relativedelta(months=delta_period) - timedelta(days=-delta_period)

    added_files_list = {}

    for commit in Repository('https://github.com/numpy/numpy.git', since=end_date, to=start_date).traverse_commits():
        for file in commit.modified_files:
            filename = file.filename
            if re.match('^.*test.*\.py$', file.filename):
                if file.change_type == file.change_type.ADD:
                    author_date = commit.author_date
                    if added_files_list.get(author_date):
                        added_files_list[author_date] = added_files_list.get(author_date) + 1
                    else:
                        added_files_list[author_date] = 1

    plt.plot(added_files_list.keys(), added_files_list.values())
    plt.xlabel('File Added Date')
    plt.ylabel('Number of Files Added')

    plt.title('Number of files added by date')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def authors_modified():
    start_date = datetime.datetime.now()
    delta_period = 6
    end_date = start_date - relativedelta(months=delta_period) - timedelta(days=-delta_period)

    author_list = {}

    for commit in Repository('https://github.com/numpy/numpy.git', since=end_date, to=start_date).traverse_commits():
        for file in commit.modified_files:
            filename = file.filename
            if re.match('^.*test.*\.py$', file.filename):
                if file.change_type == file.change_type.MODIFY:
                    if author_list.get(filename):
                        author_list.get(file.filename).add(commit.author.name)
                    else:
                        author_list[filename] = {commit.author.name}

    finaldict = {}
    index = 10
    for key, value in author_list.items():
        if index > 0:
            finaldict[key] = len(value)
            index -= 1

    plt.plot(finaldict.keys(), finaldict.values())
    plt.xlabel('File Name')
    plt.ylabel('Nr. of authors who modified the file')

    plt.title('Authors Modified Report')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


asserts_plot()
debug_assert_plot()
debug_assert_plot2()
branch_coverage()
statement_coverage()
total_coverage()
commits_by_month()
top_contributors()
total_modified()
files_added_by_date()
authors_modified()
