import pandas as pd


golf_df = pd.DataFrame([])


course = input('Enter course played: ')

holes_tot = input('Enter amount of holes played: ')


hole_no = []
for i in range(int(holes_tot)):
	hole_i = []
	hole_i.append(input('Distance: '))

