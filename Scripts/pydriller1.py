import datetime
import re
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from pydriller import Repository
import csv

start_date = datetime.datetime.now()
delta_period = 6
end_date = start_date - relativedelta(months=delta_period) - timedelta(days=-delta_period)
author_list = {}
files_list = {}
added_files_list = {}
Modified_count = 0
modified_filenames = []
for commit in Repository('https://github.com/numpy/numpy.git', since=end_date, to=start_date).traverse_commits():
    print(commit.committer_date.date().month)
    for file in commit.modified_files:
        filename = file.filename
        if re.match('^.*test.*\.py$', file.filename):
            if file.change_type == file.change_type.ADD:
                author_date = commit.author_date
                print("File {}, Authored_date {}".format(file.filename, commit.author_date))

            if file.change_type == file.change_type.MODIFY:
                if files_list.get(filename):
                    files_list[filename] = files_list.get(file.filename) + 1
                else:
                    files_list[filename] = 1

                if author_list.get(filename):
                    author_list.get(file.filename).add(commit.author.name)
                else:
                    author_list[filename] = {commit.author.name}



header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']

with open('../Outputs/test.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
