import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
from datetime import datetime, timedelta

forbidden_names = ['staff']

plt.style.use('fivethirtyeight')

data = pd.read_csv('usernames_dates.csv')

data = data[~data['username'].isin(forbidden_names)]
users = data['username']
dates = data['date']

"""
Creates plot for tracking activity by username

"""
# count occurance of activity per user
username_counter = Counter()

for user in users:
    username_counter.update([user])

#format user activity into lists
usernames = []
activity_by_user = []

for item in username_counter.most_common():
    usernames.append(item[0])
    activity_by_user.append(item[1])

usernames.reverse()
activity_by_user.reverse()

# plot
f1 = plt.figure(1)
plt.barh(usernames, activity_by_user)

plt.title('Activity By User')
plt.xlabel("# of actions in system")
plt.ylabel("user")

plt.tight_layout()

"""
Creates plot for tracking all activity over the past 14 days

"""

# create dictionary with dates as keys and values initialized to 0
last_30_days = {}
today = datetime.today()
for i in range(14):
    date = today - timedelta(days=i)
    date_string = date.strftime("%m/%d")
    last_30_days[date_string] = 0

# count occurances of activity on each date
for each in dates:
    last_30_days[each] += 1

# format activity into lists
date_list = list(last_30_days.keys())
activity_on_date = list(last_30_days.values())

# reverse to display least recent dates first
date_list.reverse()
activity_on_date.reverse()

# plot
f2 = plt.figure(2)
plt.plot(date_list, activity_on_date)

plt.title('All Activity')
plt.xlabel("date")
plt.ylabel("# of actions in system")

plt.tight_layout()

"""
Display both plots

"""

plt.show()