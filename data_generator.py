import pandas as pd
import datetime

headers = ['fname', 'lname']
names = pd.read_csv('data/names.txt', names=headers, sep=' ')

start_date = input('Enter a start date (yyyymmdd): ')
end_date = input('Enter an end date (yyyymmdd): ')

start_hour = input('Enter a start hour or "full": ').zfill(2)
end_hour = input('Enter an end hour or "full": ').zfill(2)

start = datetime.datetime( year = int(start_date[0:4]), month = int(start_date[4:6]) , day = int(start_date[6:8]), hour = int(start_hour), minute = 0, second = 0 )
end = datetime.datetime( year = int(end_date[0:4]), month = int(end_date[4:6]) , day = int(end_date[6:8]), hour = int(end_hour), minute = 0, second = 0 )

for i in range(0,3):
	
