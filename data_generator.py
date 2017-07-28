import pandas as pd
import datetime
import random

#no_lines = input('Enter desired number of lines: ')
no_lines = '9'

#dg_df = pd.DataFrame([])

headers = ['fname', 'lname']
dg_df = pd.read_csv('data/names.txt', names=headers, sep=' ')

start_date = input('Enter a start date (yyyymmdd): ')
end_date = input('Enter an end date (yyyymmdd): ')

start_hour = input('Enter a start hour or "full": ').zfill(2)
end_hour = input('Enter an end hour or "full": ').zfill(2)

start_datetime = datetime.datetime( year = int(start_date[0:4]), month = int(start_date[4:6]) , day = int(start_date[6:8]), hour = int(start_hour), minute = 0, second = 0 )
end_datetime = datetime.datetime( year = int(end_date[0:4]), month = int(end_date[4:6]) , day = int(end_date[6:8]), hour = int(end_hour), minute = 0, second = 0 )

def random_date(start, end):
	t_delta = end - start
	int_delta = (t_delta.days * 24 * 60 * 60) + t_delta.seconds
	random_second = random.randrange(int_delta)
	return start + datetime.timedelta(seconds=random_second)

date_list = []
for i in range(int(no_lines)):
	date_list.append(random_date(start_datetime, end_datetime))

dg_df['date_time'] = sorted(date_list)

