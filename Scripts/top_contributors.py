import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
from pydriller import Repository

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
# sizes_list = []
# for key, value in odict.items():
#     sizes_list.insert(value/total_commits)

# fig = plt.figure(figsize=(10, 5))
#
# # creating the bar plot
# plt.bar(month_dict.keys(), month_dict.values(), color='green',
#         width=0.4)
#
# plt.xlabel("Month")
# plt.ylabel("Total number of commits")
# plt.title("Number of commits by month")
# plt.show()
fig = plt.figure(figsize=(10, 7))
plt.pie(list(odict.values())[:10], labels=list(odict.keys())[:10])

# show plot
plt.show()