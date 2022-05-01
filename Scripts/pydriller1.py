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

with open('../Outputs/FilesAdded.csv', 'w') as f:
    header = ['File Name', 'Authored Date']
    writer = csv.writer(f)
    writer.writerow(header)
    for commit in Repository('https://github.com/numpy/numpy.git', since=end_date, to=start_date).traverse_commits():
        for file in commit.modified_files:
            filename = file.filename
            if re.match('^.*test.*\.py$', file.filename):
                if file.change_type == file.change_type.ADD:
                    data = [file.filename, commit.author_date]
                    writer.writerow(data)

                if file.change_type == file.change_type.MODIFY or file.change_type == file.change_type.RENAME:
                    if files_list.get(filename):
                        files_list[filename] = files_list.get(file.filename) + 1
                    else:
                        files_list[filename] = 1

                    if author_list.get(filename):
                        author_list.get(file.filename).add(commit.author.name)
                    else:
                        author_list[filename] = {commit.author.name}

with open('../Outputs/FilesModified.csv', 'w') as f:
    w = csv.writer(f)
    header = ['File Name', 'Modification Count']
    w.writerow(header)
    w.writerows(files_list.items())

with open('../Outputs/AuthorList.csv', 'w') as f:
    w = csv.writer(f)
    header = ['File Name', 'Authors']
    w.writerow(header)
    w.writerows(author_list.items())


