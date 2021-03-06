import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sys
import wget
import os
import random
from spacepy import pycdf
from urllib import error




def daterange( start_date, end_date ):
    if start_date <= end_date: #
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )

#==============Choosing Dataset

'''
1 - GOES Proton Flux
2 - Wind Type III Radio Bursts
3 - Neutron Monitor Counts
4 - ACE/Wind Solar Wind Speed'
5 - GOES-15 Xray Flux
'''

''' # testing new plotting scheme
print(f'{"="*40}\n{"=" + "DATASETS".center(38," ") + "="}\n{"="*40}\n1 - GOES-15 Proton Flux\n2 - Wind Type III Radio Bursts\n3 - Neutron Monitor Counts\n4 - ACE/Wind Solar Wind Speed\n5 - GOES-15 Xray Flux\n{"="*40}')


option_bin_set = set()
while True: # energy_bin != 'done':
	option_bin = input('Enter Dataset Option then "done" or "all": ').lower()
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

			if len(option_bin_set) > 4:
				print('SELECTION ERROR: Only 4 datasets are allowed per canvas.')
				sys.exit(0)

	elif option_bin == 'done':
		break
'''


# ========== Reading in CSV
data_df = pd.read_csv('output/data_sample.csv')




#=========== Plotting Data
'''
1 - GOES-15 Proton Flux
2 - Wind Type III Radio Bursts
3 - Neutron Monitor Counts
4 - ACE/Wind Solar Wind Speed'
'''

''' # testing new plotting scheme
length_data = int(len(option_bin_set))
length_data_list = []
for i in range(length_data):
	length_data_list.append(i)


j = -1
def next():
	global j
	if (j < length_data+2):
		j += 1
	#print(length_data_list[j])


def applyPlotStyle():
	axes[length_data_list[j]].grid(True)
	axes[length_data_list[j]].minorticks_on()


if length_data > 1:
	f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=False, figsize=(10, 6))

if length_data == 1:
	length_data_list[0] = 0,0
	f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=True, figsize=(10, 6), squeeze=False)
'''



#high_bin_proton = sorted(energy_bin_list[-1])[1]
#low_bin_proton = sorted(energy_bin_list[0])[1]

#high_bin_proton_str = sorted(energy_bin_list[-1])[0]
#low_bin_proton_str = sorted(energy_bin_list[0])[0]






	
''' # uncomment for final write of code
	axes[length_data_list[j]].legend(loc='lower right', ncol=1,fontsize=8)# borderaxespad=0)# bbox_to_anchor=(1, 0.5)) # bbox_to_anchor=(1.02,1.0)
	if '1' in option_bin_set:
		high_bin_proton = sorted(energy_bin_list)[-1][0]
		low_bin_proton = sorted(energy_bin_list)[0][0]

		high_bin_proton_str = sorted(energy_bin_list)[-1][1]
		low_bin_proton_str = sorted(energy_bin_list)[0][1]
		axes[length_data_list[j]].axvline(proton_df[f'{low_bin_proton}'].idxmax()) # (proton_df.P6W_UNCOR_FLUX.max())
	
'''
	# axes[length_data_list[j]].axvline(proton_df.idxmax().P6W_UNCOR_FLUX) # (proton_df.P6W_UNCOR_FLUX.max())





# =========== Choose which data to plot

plotter_choice = set()
while True: # energy_bin != 'done':
	plot_option_bin = input('Enter plotting option(s) or "all": ').lower()
	if plot_option_bin != 'done':
		if plot_option_bin == 'all':
			'''
			for i in data_df.columns:
				if isinstance(data_df[f'{i}'][0], str) == False:
					plotter_choice.add(f'{i}')
			'''
			plotter_choice.add('plotting')
			plotter_choice.add('plotting')
			break
		
		elif len(plotter_choice) < 2:
			plotter_choice.add(plot_option_bin)
			'''
			if len(option_bin_set) > 4:
				print('SELECTION ERROR: Only 4 datasets are allowed per canvas.')
				sys.exit(0)
			'''
	elif plot_option_bin == 'done':
		break

'''
plotter_choice = list(plotter_choice)
if x_input == plotter_choice:
	print('SELECTION ERROR: Only unique column data may be chosen.')
	sys.exit(0)
'''





# plot_choice = input('Enter plot option (plot or map): ')

# ======== choices
if 'plot' in plotter_choice: # here for testing, remove when projection is complete

	print(f'{"="*40}\n{"=" + "X".center(38," ") + "="}\n{"="*40}')
	
	data_set_count = 1
	for i in data_df.columns:
		if isinstance(data_df[f'{i}'][0], str) == True:
			option_str = '  (Only available for x-axis)'
		else:
			option_str = ''
		print(str(data_set_count) + '. ' + str(i) + f'{option_str}')
	
		data_set_count += 1
	print(f'{"="*40}')





	x_input = input('Choose x-axis data: ').lower()
	
	
	print(f'\n{"="*40}\n{"=" + "Y".center(38," ") + "="}\n{"="*40}')
	
	
	data_set_count = 1
	for i in data_df.columns:
		if isinstance(data_df[f'{i}'][0], str) == False:
				print(str(data_set_count) + '. ' + str(i))
				data_set_count += 1
	
	print(f'{"="*40}')
	
	'''
	option_y = input('Enter number of y-data: ')
	
	y_input = []
	for i in range(int(option_y)):
		y_input.append(input('Choose y-axis data: '))
	'''
	
	
	y_input = set()
	while True: # energy_bin != 'done':
		option_bin = input('Enter y-axis data then "done" or "all": ').lower()
		if option_bin != 'done':
			if option_bin == 'all':
				for i in data_df.columns:
					if isinstance(data_df[f'{i}'][0], str) == False:
						y_input.add(f'{i}')
	
				break
			
			elif len(y_input) < data_set_count:
				y_input.add(option_bin)
	
				'''
				if len(option_bin_set) > 4:
					print('SELECTION ERROR: Only 4 datasets are allowed per canvas.')
					sys.exit(0)
				'''
		elif option_bin == 'done':
			break
	
	y_input = list(y_input)
	
	
	if x_input == y_input:
		print('SELECTION ERROR: Only unique column data may be chosen.')
		sys.exit(0)
	
	
	data_df.set_index(f'{x_input}').plot(y=y_input,marker="o", rot=45, grid=True, figsize=(11,7)) # data_df[f'{y_input}']
	
	
	
	#plt.plot(data_df[f'{x_input}'], data_df[f'{y_input}'], 'o')
	
	plt.xlabel(f'{x_input}', fontname='Arial', fontsize=12)
	plt.ylabel(f'{y_input}', fontname='Arial', fontsize=12)
	
	# data_df.plot(rot=45) #kind='bar',alpha=0.75, rot=0)
	 #, horizontalalignment='center')
	# plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
	plt.tight_layout()
	plt.show()


# if (x_input == 'lat' and y_input == 'long') or (y_input == 'lat' and x_input == 'long') or :
'''
option_map = input('Plot latitude and longitude projection? (yes or no): ') # for testing commment this line until projections are complete
if option_map == 'yes':
'''


if 'map' in plotter_choice:
	# ======= Projection (Basemap solution) # deprecated, but kept for reference when building cartopy solution
	'''
	from mpl_toolkits.basemap import Basemap
	from matplotlib.pyplot import cm

	# lon_0 is central longitude of projection.
	lats = list(data_df['lat'])
	lons = list(data_df['long'])
	
	# resolution = 'c' means use crude resolution coastlines.
	proj_choice = 'hammer'

	plt.figure(figsize=(10,6))
	m = Basemap(projection=f'{proj_choice}',lon_0=0,resolution='c') # lon_0 = 0 # default used was 'robin'
	m.drawcoastlines()
	m.fillcontinents(color='green',lake_color='aqua') #coral
	# draw parallels and meridians.
	m.drawparallels(np.arange(-90.,120.,30.), labels=[1,0,0,0])
	m.drawmeridians(np.arange(0.,420.,60.)) # , labels=[1,0,0,0])
	m.drawmapboundary(fill_color='aqua')
	plt.title(f"{proj_choice} Projection".title())
	
	x, y = m(lons,lats)
	# plt.plot(x,y, 'o', color='blue')
	m.scatter(x,y,10,marker='o',color='red', zorder=5)


	citin_x, citin_y = m(list(data_df['city_long_in']), list(data_df['city_lat_in']))
	citout_x, citout_y = m(list(data_df['city_long_out']), list(data_df['city_lat_out']))

	
	color_cm=iter(cm.viridis(np.linspace(0,1, len(data_df))))

	for i in range(len(data_df)):

		color_choice = next(color_cm)
		m.drawgreatcircle(list(data_df['city_long_in'])[i],list(data_df['city_lat_in'])[i],list(data_df['city_long_out'])[i],list(data_df['city_lat_out'])[i],linewidth=1,color=color_choice, zorder=4)
	


	# plt.tight_layout()

	plt.show()
	'''
	# ======= Projection (cartopy solution)
	import cartopy.crs as ccrs
	from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
	from matplotlib.pyplot import cm

	proj_choice = ccrs.PlateCarree() # Mollweide is the closest to aitoff

	plt.figure(figsize=(10,6))
	ax = plt.axes(projection=proj_choice) # PlateCarree and Mercator have functioning gridlines
	ax.stock_img()
	plt.title('Plate Carree Projection')

	
	gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, zorder=2)
	gl.xlabels_top = False
	gl.xformatter = LONGITUDE_FORMATTER
	gl.yformatter = LATITUDE_FORMATTER
	

	#plt.plot([ny_lon, delhi_lon], color='gray', transform=ccrs.PlateCarree())


	color_cm=iter(cm.viridis(np.linspace(0,1, len(data_df))))

	for i in range(len(data_df)):
		color_choice = next(color_cm)

		plt.plot(list(data_df['long'])[i],list(data_df['lat'])[i], 'o', color='red', transform=ccrs.Geodetic(), markersize=2, zorder=3)
		plt.plot([list(data_df['city_long_in'])[i],list(data_df['city_long_out'])[i]] , [list(data_df['city_lat_in'])[i],list(data_df['city_lat_out'])[i]] , color=color_choice, linewidth=1,marker='o', markersize=1, transform=ccrs.Geodetic(), zorder=4) # , marker='.'


	plt.show()




'''
elif option_map == 'no':
	print('No projection generated.')
	sys.exit(0)
'''



sys.exit(0)



j = -1
def next():
	global j
	if (j < length_data+2):
		j += 1


#======dataset plotting
'''
from mpl_toolkits.basemap import Basemap
# lon_0 is central longitude of projection.
lats = list(data_df['lat'])
lons = list(data_df['long'])

# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='hammer',lon_0=0,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='green',lake_color='aqua') #coral
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,120.,30.), labels=[1,0,0,0])
m.drawmeridians(np.arange(0.,420.,60.)) # , labels=[1,0,0,0])
m.drawmapboundary(fill_color='aqua')
plt.title("Hammer Projection")

x, y = m(lons,lats)
# plt.plot(x,y, 'o', color='blue')
m.scatter(x,y,10,marker='o',color='red')

plt.show()
'''



if '1' in option_bin_set:
	next()
	name_no = list(range(len(data_df)))
	fname_list = list(data_df['fname'])
	lname_list = list(data_df['lname'])
	'''
	for i in sorted(energy_bin_list):
		axes[length_data_list[j]].plot(data_df['fname'], data_df['payload'], color=f'{i[2]}', label= f'{i[1]}')#, logy=True)
	'''
	#axes[length_data_list[j]].xticks(name_no, fname_list, rotation=45)
	axes[length_data_list[j]].plot(name_no, data_df['payload'], color='blue', label= 'blah')#, logy=True)
	axes[length_data_list[j]].set_yscale('log')
	axes[length_data_list[j]].set_ylabel(f'GOES- Proton\nFlux [pfu]', fontname="Arial", fontsize = 12)
	plt.sca(axes[length_data_list[j]])
	plt.xticks(name_no, fname_list, rotation=45)
	applyPlotStyle()



if '2' in option_bin_set:
	next()
	axes[length_data_list[j]].plot(data_df['doy'],data_df['payload'], 'o', color='navy', label= '20 kHz - 1040 kHz')
	axes[length_data_list[j]].set_ylabel('Wind Type III\nRadio Burst [sfu]', fontname="Arial", fontsize = 12)
	applyPlotStyle()


if '3' in option_bin_set:
	next()
	color_count = []

	for i in sorted_nm_list:
	
		color_list = ['red','orange','green','blue','indigo','violet','purple'] #,'yellow'
		color_list = list(set(color_list) - set(color_count))
	
		rand_color = random.choice(color_list)
		color_count.append(rand_color)
	
		axes[length_data_list[j]].plot(nm_data[f'{i}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=rand_color, label=f'{i}')
	axes[length_data_list[j]].set_ylabel('Neu. Monitor\n[counts/s]', fontname="Arial", fontsize = 12)
	applyPlotStyle()

if '4' in option_bin_set:
	next()
	axes[length_data_list[j]].plot(wind_data['wind_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='Wind: Ion Bulk Flow Speed GSE')
	axes[length_data_list[j]].plot(ace_data['ace_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label='ACE: H Bulk Speed')
	axes[length_data_list[j]].set_ylabel('Solar Wind\nSpeed [km/s]', fontname="Arial", fontsize = 12)
	applyPlotStyle()

if '5' in option_bin_set:
	next()
	axes[length_data_list[j]].plot(xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label='0.1-0.8 nm')
	axes[length_data_list[j]].plot(xray_df['A_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='0.05-0.4 nm')
	axes[length_data_list[j]].set_yscale('log')
	axes[length_data_list[j]].set_ylabel('GOES-15 Xray\nFlux [Wm$^2$]', fontname="Arial", fontsize = 12)
	applyPlotStyle()



plt.xlabel('Time (UT)', fontname="Arial", fontsize = 12)

myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

#ax = plt.gca() # commented to get rid of datetime axis
#ax.xaxis.set_major_formatter(myFmt)
#plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')

plt.suptitle(f'Space Weather Monitor', fontname="Arial", fontsize = 14) #, y=1.04,
#plt.tight_layout()

plt.subplots_adjust(wspace = 0, hspace = 1, top=0.91)
#plt.savefig('omni_test_legacy.png', format='png', dpi=900)

plt.show()
