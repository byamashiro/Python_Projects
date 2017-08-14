import pandas as pd
import datetime
import random
from geopy.geocoders import Nominatim
import time
import sys
import numpy as np
import os


# ============== Data generator
print(f'{"="*40}\n{"=" + "Data Generator".center(38," ") + "="}\n{"="*40}')

no_lines = input('Enter desired number of lines: ')
#no_lines = '20'

#dg_df = pd.DataFrame([])


# ============= Name Column
#headers = ['fname', 'lname'] # original names file
#dg_df = pd.read_csv('data/names.txt', names=headers, sep=' ')

dg_df = pd.DataFrame([])
print('[x] Data Frame Generated.')

first_name = pd.read_csv('data/CSV_Database_of_First_Names.csv', header=0, index_col=False)
last_name = pd.read_csv('data/CSV_Database_of_Last_Names.csv', header=0, index_col=False)

dg_df['fname'] = np.random.choice(first_name['firstname'], int(no_lines))
dg_df['lname'] = np.random.choice(last_name['lastname'], int(no_lines))
print('[x] Names generated.')

#sys.exit(0)


# =============  Datetime Column
# Uncomment when program is complete
start_date = input('Enter a start date (yyyymmdd): ')
if start_date == '':
	start_date = '20120307'
	end_date = '20120310'
	start_hour = '00'
	end_hour = '00'

elif start_date != '':
	end_date = input('Enter an end date (yyyymmdd): ')
	start_hour = input('Enter a start hour (hh): ').zfill(2) #  or "full"
	end_hour = input('Enter an end hour (hh): ').zfill(2) #  or "full"

'''

'''
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
dg_df['dtime'] = dg_df['date_time']


unix_list = []
for i in range(len(dg_df)):
	unix_list.append(int(time.mktime(dg_df['date_time'][i].timetuple())*1e3 + dg_df['date_time'][i].microsecond/1e3)/1000) # time.mktime(dg_df['date_time'][0].timetuple())

dg_df['unix_time'] = sorted(unix_list) # UNIX time



doy_list = []
for i in range(len(dg_df)):
	doy_list.append((dg_df['date_time'][i].timetuple()).tm_yday)

dg_df['doy'] = doy_list # day of year # was sorted(doy_list), but changed
	
dg_df.set_index(keys='date_time' , inplace=True)
print('[x] Datetimes generated.')
# sys.exit(0)
# ============= Email domains
email_domains = pd.read_csv('data/free_email_provider_domains.txt', names=['domain'], comment='#')

email_list = []
email_address = email_domains['domain'].tolist()
for i in range(len(dg_df)):
	email_list.append(random.choice(email_address))

dg_df['email_address'] = dg_df.fname.astype(str).str[0] + dg_df.lname + '@' + email_list
print('[x] Email addresses generated.')
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
print('[x] IP Addresses generated.')
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
print('[x] Latitude and longitude generated.')

# =======payload
payload_list = []
for i in range(len(dg_df)):
	payload_list.append(random.randint(0,1000000))

dg_df['payload'] = payload_list
print('[x] Payload generated.')

# ======= city in / city out # still working


cit_data = pd.read_csv('data/cit_data.txt', sep=',')

cit_lat = []
for i in cit_data['Latitude']:
	if i.endswith('N'):
		lat_n = i.rstrip('N')
		cit_lat.append(float('+' + lat_n))
	elif i.endswith('S'):
		lat_s = i.rstrip('S')
		cit_lat.append(float('-' + lat_s))


cit_long = []
for i in cit_data['Longitude']:
	if i.endswith('E'):
		long_n = i.rstrip('E')
		cit_long.append(float('+' + long_n))
	elif i.endswith('W'):
		long_s = i.rstrip('W')
		cit_long.append(float('-' + long_s))

cit_data['city_lat'] = cit_lat
cit_data['city_long'] = cit_long

dg_df['country'] = np.random.choice(cit_data['Country'], int(no_lines))

cit_data.set_index('Country', inplace=True)


cit_cap = []
cit_lat = []
cit_long = []

for i in dg_df['country']:
	cit_cap.append(cit_data['Capital'].loc[f'{i}'])
	cit_lat.append(cit_data['city_lat'].loc[f'{i}'])
	cit_long.append(cit_data['city_long'].loc[f'{i}'])



# dg_df['city_lat'] = np.random.choice(cit_data['city_lat'], int(no_lines))
# dg_df['city_long'] = np.random.choice(cit_data['city_long'], int(no_lines))


print('[x] Latitude and longitude generated.')




# ========= Corruption
dg_list_multi = [x for x in dg_df.columns if not 'date_time' in x] # dg_list = list(dg_df.columns)
print(f'{"="*40}\n{"=" + "Corruption Options".center(38," ") + "="}\n{"="*40}')
for i in dg_list_multi:
	print(i)
print('=' * 40)

#print(dg_list_multi)

corr_bin_set = set()

while True: # energy_bin != 'done':
	corr_bin = input('Enter Corruption Option(s) then "done" or "all" or "none": ').lower() #  or "all"
	if corr_bin == 'none':
		print('No corruption generated.')
		break

	elif corr_bin != 'done':
		if corr_bin == 'all':

			corrupt_perc = input('Enter amount of corruption (0-100%): ')

			if int(corrupt_perc) > 100 or int(corrupt_perc) < 0:
				print('PERCENTAGE ERROR: Input a value between 0% and 100%.')
				sys.exit(0)
			corr_tot = int(dg_df.size * (int(f'{corrupt_perc}')/100))
			uncorr_tot = int(dg_df.size) - int(dg_df.size * (int(f'{corrupt_perc}')/100))

			while dg_df.count().sum() >= uncorr_tot+1:
			#print(dg_df.count().sum())
				rand_corr = random.choice(dg_list_multi)
				rand_corr_int = random.randint(0, int(no_lines)-1)
				if dg_df[f'{rand_corr}'][rand_corr_int] != np.nan:
					dg_df.replace(dg_df[f'{rand_corr}'][rand_corr_int], value=np.nan, inplace=True)
			
			print(f'[x] Full dataframe corruption for {corr_tot}/{dg_df.size} data values generated.')

			break
		

		#elif int(corr_bin) < len(dg_list_multi)+1:
		else:
			corr_bin_set.add(corr_bin)

			if len(corr_bin_set) > 5:
				print('SELECTION ERROR: Only 4 datasets are allowed per canvas.')
				sys.exit(0)

	elif corr_bin == 'done':
		break


for i in corr_bin_set:
	corrupt_perc = input(f'Enter amount of corruption for column {i} (0-100%): ')
	if int(corrupt_perc) > 100 or int(corrupt_perc) < 0:
		print('PERCENTAGE ERROR: Input a value between 0% and 100%.')
		sys.exit(0)
	
	corr_tot = int(int(no_lines) * (int(f'{corrupt_perc}')/100))
	uncorr_tot = int(no_lines) - int(int(no_lines) * (int(f'{corrupt_perc}')/100))
	
	while dg_df[i].count().sum() >= uncorr_tot+1:
		#print(dg_df.count().sum())
		#rand_corr = random.choice(dg_list_multi)
		rand_corr_int = random.randint(0, int(no_lines)-1)
		if dg_df[i][rand_corr_int] != np.nan:
			dg_df.replace(dg_df[i][rand_corr_int], value=np.nan, inplace=True)
	print(f'[x] {i} : Column-wise corruption for {corr_tot}/{no_lines} data values generated.')



# ======== testing row corruption
'''

corrupt_row_perc = input(f'Enter amount of corruption for column {i} (0-100%): ')
if int(corrupt_row_perc) > 100 or int(corrupt_row_perc) < 0:
	print('PERCENTAGE ERROR: Input a value between 0% and 100%.')
	sys.exit(0)

corr_tot = int(int(no_lines) * (int(f'{corrupt_row_perc}')/100))
uncorr_tot = int(no_lines) - int(int(no_lines) * (int(f'{corrupt_row_perc}')/100))

# add the percentages based off of number of rows and total percentage based on rows not single elements in dataframe

for i in 
	rand_index = random.choice(dg_df.index)
	rand_row = dg_df.loc[rand_index]

'''
# ======= OUTPUT
print(f'{"="*40}\n{"=" + "Output Options".center(38," ") + "="}\n{"="*40}\n1 - CSV\n2 - ASCII\n3 - JSON\n4 - PKL\n5 - SQL\n6 - CDF\n{"="*40}')


option_bin_set = set()
while True: # energy_bin != 'done':
	option_bin = input('Enter Output Option(s) then "done" or "none": ').lower() #  or "all"
	if option_bin == 'none':
		print('No outputs generated.')
		break

	elif option_bin != 'done':
		if option_bin == 'all':
			option_bin_set.add('1')
			option_bin_set.add('2')
			option_bin_set.add('3')
			option_bin_set.add('4')
			option_bin_set.add('5')
			option_bin_set.add('6')
			break
		
		elif int(option_bin) < 7:
			option_bin_set.add(option_bin)

			if len(option_bin_set) > 6:
				print('SELECTION ERROR: Only 4 datasets are allowed per canvas.')
				sys.exit(0)

	elif option_bin == 'done':
		break

	
	
	


output_name = 'data_sample'


# ======= output to csv
if '1' in option_bin_set:
	delim_opt = input('Choose delimiter character for .csv output: ')
	dg_df.to_csv(f'output/{output_name}.csv', sep=f'{delim_opt}', index=False)
	print('[x] Output as CSV generated.')
# ======= output to ascii
if '2' in option_bin_set:
	dg_df.to_csv(f'output/{output_name}.txt', sep='\t', index=False)
	print('[x] Output as TXT generated.')

# ======= output to json
if '3' in option_bin_set:
	dg_df.to_json(f'output/{output_name}.JSON', orient='table')
	print('[x] Output as JSON generated.')

# ======= output to pickle
if '4' in option_bin_set:
	dg_df.to_pickle(f'output/{output_name}.pkl')
	print('[x] Output as PKL generated.')

# ======= output to SQL
if '5' in option_bin_set:
	#delim_opt = input('Choose delimiter character: ')
	import sqlite3
	conn = sqlite3.connect('output/data_sample.db')
	dg_df.to_sql('gen_data', con=conn, if_exists='replace')
	conn.close()
	print('[x] Output as SQL generated.')


# ======= output to cdf

if '6' in option_bin_set:
	os.remove(f'output/{output_name}.cdf')
	from spacepy import pycdf


	cdf = pycdf.CDF(f'output/{output_name}.cdf', '')
	for i in dg_list_multi:
		try:
			cdf[i] = dg_df[i]
		except ValueError as val_err:
			print(f'The {i} column was not added to the output CDF file.')
		else:
			print(f'The {i} column was not added to the output CDF file.')
	#cdf['date_time'] = dg_df['dtime']

	cdf.attrs['Author'] = 'Bryan Yamashiro'
	cdf.attrs['CreateDate'] = datetime.datetime.now()
	cdf.close()





# ======== check if script works
#print(dg_df)

''' test json
import json
import pprint as pprint
with open('data_sample.JSON') as inputfile:
	json_example = json.load(inputfile)
	pprint(json_example)
'''
''' test sql
conn = sqlite3.connect('data_gen.db')
df = pd.read_sql_query('SELECT * FROM gen_data LIMIT 5', conn)	
'''                                                           		



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



