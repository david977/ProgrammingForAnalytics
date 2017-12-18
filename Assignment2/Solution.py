import pandas as pd 
import numpy
import csv
'''we get the total population for every year'''
data = pd.read_csv('indicator_total_population_cleaned.txt', sep=';')
years = list(data.columns.values)[1:]
total_populations = [] #total population of world for each year
for yr in years:
	total_populations.append(data[yr].sum())



def Number_Checker():
	'''This function replaces non numbers in population with 'Not Available' and each absolute number is replaced with percentage
		and also saves the contents into new file called newpopulation.txt
	'''
	with open('indicator_total_population_cleaned.txt') as f, open('newpopulation.txt','a', newline='') as b:
		reader = csv.reader(f, delimiter=';')
		writer = csv.writer(b, delimiter=';')
		headers = next(reader)
		writer.writerow(headers)
		next(reader)
		for row in reader:
				row_to_write=[row[0]]
				for population in zip(row[1:], total_populations):
					#convert absolute values to % and also handle missing data
					try:
						row_to_write.append(((float(population[0])/ population[1]))*100)
					except ValueError:
						row_to_write.append('Not Available')
				writer.writerow(row_to_write)

Number_Checker()
