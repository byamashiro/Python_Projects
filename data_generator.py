import pandas as pd
import datetime
import random
from geopy.geocoders import Nominatim
import time
import sys

#no_lines = input('Enter desired number of lines: ')
no_lines = '9'

#dg_df = pd.DataFrame([])


# ============= Name Column
headers = ['fname', 'lname']
dg_df = pd.read_csv('data/names.txt', names=headers, sep=' ')


# =============  Datetime Column
''' # Uncomment when program is complete
start_date = input('Enter a start date (yyyymmdd): ')
end_date = input('Enter an end date (yyyymmdd): ')
start_hour = input('Enter a start hour or "full": ').zfill(2)
end_hour = input('Enter an end hour or "full": ').zfill(2)
'''

start_date = '20120307'
end_date = '20120310'
start_hour = '00'
end_hour = '00'

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
pd.set_option('display.float_format', lambda x: '%.3f' % x)

dg_df['date_time'] = sorted(date_list)



unix_list = []
for i in range(len(dg_df)):
	unix_list.append(int(time.mktime(dg_df['date_time'][i].timetuple())*1e3 + dg_df['date_time'][i].microsecond/1e3)/1000) # time.mktime(dg_df['date_time'][0].timetuple())

dg_df['unix_time'] = sorted(unix_list)



doy_list = []
for i in range(len(dg_df)):
	doy_list.append((dg_df['date_time'][i].timetuple()).tm_yday)

dg_df['doy'] = sorted(doy_list)
	

# sys.exit(0)
# ============= Email domains
email_domains = pd.read_csv('data/free_email_provider_domains.txt', names=['domain'], comment='#')

email_list = []
email_address = email_domains['domain'].tolist()
for i in range(len(dg_df)):
	email_list.append(random.choice(email_address))

dg_df['email_address'] = dg_df.fname.astype(str).str[0] + dg_df.lname + '@' + email_list

# =========== IP Addresses

# ===== toip
ipv4_toip_list = []
for i in range(len(dg_df)):
	ipv4_toip_list.append(str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)))

dg_df['toip'] = ipv4_toip_list

# ===== fmip
ipv4_fmip_list = []
for i in range(len(dg_df)):
	ipv4_fmip_list.append(str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)))

dg_df['fmip'] = ipv4_fmip_list

# ============= Latitude Longitude
geolocator = Nominatim()
#location = geolocator.geocode("175 5th Avenue NYC")

loc_list = []
lat_list = []
long_list = []

latlong_check = input('Check Latitude and Longitude (yes or no) - use "no" for time saving: ')

if latlong_check == 'yes':
	while True:
		r_lat = round(random.uniform(-90.0, 90.0),6)
		r_long = round(random.uniform(-180.0, 180.0),6)
		location = geolocator.reverse(f"{r_lat}, {r_long}", language='en', timeout=3) # timeout=None
	
	
		if location.address == None:
			continue
	
		if location.address != None:
			loc_list.append(location.address.encode('utf-8').strip()) # .encode('utf-8').strip()) # 'utf-8' # 'ascii', 'ignore'
			# loc_list.append(location.address.decode('unicode_escape').encode('ascii', 'ignore'))
			# print(location.address.encode('utf-8').strip())
			lat_list.append(r_lat)
			long_list.append(r_long)
	
	
		if len(loc_list) == int(no_lines):
			break

	dg_df['loc'] = loc_list

if latlong_check == 'no':
	while True:
		r_lat = round(random.uniform(-90.0, 90.0),6)
		r_long = round(random.uniform(-180.0, 180.0),6)
	
		lat_list.append(r_lat)
		long_list.append(r_long)

		if len(lat_list) == int(no_lines):
			break
	
dg_df['lat'] = lat_list
dg_df['long'] = long_list

# =======payload
payload_list = []
for i in range(len(dg_df)):
	payload_list.append(random.randint(0,1000000))

dg_df['payload'] = payload_list



# ======= OUTPUT
print(f'{"="*40}\n{"=" + "Output Options".center(38," ") + "="}\n{"="*40}\n1 - .csv\n2 - .txt\n3 - .JSON\n4 - .pickle\n5 - .sql\n{"="*40}')


option_bin_set = set()
while True: # energy_bin != 'done':
	option_bin = input('Enter Output Option then "done" or "all": ').lower()
	if option_bin != 'done':
		if option_bin == 'all':
			option_bin_set.add('1')
			option_bin_set.add('2')
			option_bin_set.add('3')
			option_bin_set.add('4')
			option_bin_set.add('5')
			break
		
		elif int(option_bin) < 6:
			option_bin_set.add(option_bin)

			if len(option_bin_set) > 5:
				print('SELECTION ERROR: Only 4 datasets are allowed per canvas.')
				sys.exit(0)

	elif option_bin == 'done':
		break

	elif option_bin == 'none':
		print('No outputs generated.')
		break


output_name = 'test'


# ======= output to csv
if '1' in option_bin_set:
	delim_opt = input('Choose delimiter character for .csv output: ')
	dg_df.to_csv(f'output/{output_name}.csv', sep=f'{delim_opt}', index=False)

# ======= output to ascii
if '2' in option_bin_set:
	#delim_opt = input('Choose delimiter character: ')
	dg_df.to_csv(f'output/{output_name}.txt', sep='\t', index=False)

# ======= output to json
if '3' in option_bin_set:
	#delim_opt = input('Choose delimiter character: ')
	dg_df.to_json(f'output/{output_name}.JSON', index=False)

# ======= output to pickle
if '4' in option_bin_set:
	#delim_opt = input('Choose delimiter character: ')
	dg_df.to_picle(f'output/{output_name}.pickle', index=False)

# ======= output to SQL
if '5' in option_bin_set:
	#delim_opt = input('Choose delimiter character: ')
	dg_df.to_sql(f'output/{output_name}.sql', index=False)



# ======== check if script works
print(dg_df)

		



'''
	if location.address == None:
		print('Recalibrating...')
		r_lat = round(random.uniform(-90.0, 90.0),6)
		r_long = round(random.uniform(-180.0, 180.0),6)
		location = geolocator.reverse(f"{r_lat}, {r_long}", timeout=None)
		continue
	else:
		print(location.address.encode('utf-8').strip())
'''



