import os
import csv
import numpy

path = '/Users/shuyiqi/Desktop/MAT-209/data_all'

treatments = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
years = ['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014']

header = 'Area,Year,Crops Primary(MT),Crops Processed(MT),Live Animals(M Heads),Livestock Primary(MT),Livestock Processed(MT),CO2eq(gg)\n'

m = len(treatments)
n = len(years)
crops = numpy.zeros((n,m), dtype=float)
crops_processed = numpy.zeros((n,m), dtype=float)
live_animals = numpy.zeros((n,m), dtype = float)
LS_primary = numpy.zeros((n,m), dtype=float)
LS_processed = numpy.zeros((n,m), dtype=float)
CO2eq = numpy.zeros((n,m), dtype=float)


with open('output_all.csv', mode='w') as output_file:
    output_file.write(header)
    for filename in os.listdir(path):
        with open(path+'/'+filename, mode='rU') as csv_file:
                csv_reader = csv.reader(x.replace('\0', '') for x in csv_file)
                line_count = 0
                var = ''
                domain = ''
                is_float = 0
                for splitted_row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    elif line_count == 1:
                        var = splitted_row[0]
                        x = treatments.index(splitted_row[1])
                        y = years.index(splitted_row[4])
                        if (var == 'Crops'):
                            crops[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)/1000000.0
                        elif (var == 'Crops processed'):
                            crops_processed[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)/1000000.0
                        elif (var == 'Livestock Primary'):
                            LS_primary[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)/1000000.0
                        elif (var == 'Live Animals'):
                            if (splitted_row[5] == 'Head'):
                                live_animals[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)/1000000.0
                            else:
                                live_animals[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)/1000.0
                        elif (var == 'Livestock Processed'):
                            LS_processed[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)/1000000.0
                        elif (var == 'Agriculture Total'):
                            CO2eq[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)
                        line_count += 1
                    else:
                        x = treatments.index(splitted_row[1])
                        y = years.index(splitted_row[4])
                        if (var == 'Crops'):
                            crops[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)/1000000.0
                        elif (var == 'Crops processed'):
                            crops_processed[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)/1000000.0
                        elif (var == 'Live Animals'):
                            if (splitted_row[5] == 'Head'):
                                live_animals[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)/1000000.0
                            else:
                                live_animals[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)/1000.0
                        elif (var == 'Livestock Primary'):
                            LS_primary[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)/1000000.0
                        elif (var == 'Livestock Processed'):
                            LS_processed[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)/1000000.0
                        elif (var == 'Agriculture Total'):
                            CO2eq[y][x] += float(splitted_row[6] if len(splitted_row[6])!=0 else 0)
                        line_count += 1
    for i in range(0, n):
        for j in range(0, m):
            to_write = str(treatments[j])+','+str(years[i])+','+str(crops[i][j])+','+str(crops_processed[i][j])+','+str(live_animals[i][j])+','+str(LS_primary[i][j])+','+str(LS_processed[i][j])+','+str(CO2eq[i][j])+'\n'
            output_file.write(to_write)
