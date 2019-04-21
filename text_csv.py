#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import csv
import io
from itertools import izip

#reading the text file converted from R script
filne = "r_output.txt"
list_final = []

with open(filne,'r+') as f:
    data = f.readlines()

import codecs
fout=codecs.open('basic_details.csv','wb','utf-8')
fout.write("Sate;" + "District Name;" + "Village Name;" + "Cluster Name;" + "Block Name;" + "School Code & Name;" + "PINCODE;" + "Name of Head Master;" + "Management;" + "School Category;" + "Type of School;" + "Location;"  + "Lowest Class;" + "Highest Class;" + "Year of Establishment;" + "Approachable by all weather road;"  + "Shift School;" + "Special Sch for CWSN;" + "Visits by Resource Tch. for CWSN;" + "Residential School;" + "Academic Inspections;" + "Visits by CRC Coordinator;" + "Visits by Block Level Officer;" + "Pre-Primary Section;" + "Total Students (Pre-Primary);" + "Total Teachers (Pre-Primary);" + "Affiliation Board for Sec.;" + "Streams available;" + "Affiliation Board for H.Sec.\n")

# fout_details=codecs.open('final_details.csv','wb','utf-8') 
# fout_details.write("Management," + "School Category," + "Type of School," + "Location,"  + "Lowest Class," + "Highest Class," + "Year of Establishment," + "Approachable by all weather road,"  + "Shift School," + "Special Sch for CWSN," + "Visits by Resource Tch. for CWSN," + "Residential School," + "Academic Inspections," + "Visits by CRC Coordinator," + "Visits by Block Level Officer," + "Pre-Primary Section," + "Total Students (Pre-Primary)," + "Total Teachers (Pre-Primary)," + "Affiliation Board for Sec.," + "Streams available," + "Affiliation Board for H.Sec.\n")

for line in data :
    list_final.append(line.split())    
print(list_final[9])
State = ''
District_Name = ''
Village_Name = ''
Cluster_Name = ''
Block_Name = ''
School_code_Name = ''
PINCODE = ''
Name_of_HeadMaster = ''
Management = ''
School_Type = ''
School_Category = ''
Location = ''
Lowest_Class = ''
Highest_Class = ''
Year_estab = ''
Weather_road = ''
Shift_school = ''

flag_state = 0
flag_district = 0
for i in range(2,len(list_final[2])):
    if list_final[2][i-1] ==  'State':
        flag_state = 1
    if list_final[2][i] == 'District':
        flag_state = 0
    if flag_state == 1:
        State += list_final[2][i] + ' ' 
    if list_final[2][i-1] == 'Name' and list_final[2][i-2] == 'District':
        flag_district = 1
    if flag_district == 1:
        District_Name += list_final[2][i] + ' '

flag_village = 0
flag_cluster = 0
for i in range(2,len(list_final[3])):
    if list_final[3][i-1] ==  'Name' and list_final[3][i-2] == 'Village':
        flag_village = 1
    if list_final[3][i] == 'Cluster':
        flag_village = 0
    if flag_village == 1:
        Village_Name += list_final[3][i] + ' '
    if list_final[3][i-1] == 'Name' and list_final[3][i-2] == 'Cluster':
        flag_cluster = 1
    if flag_cluster == 1:
        Cluster_Name += list_final[3][i] + ' '

flag_block = 0
flag_school_code = 0
for i in range(2,len(list_final[4])):
    if list_final[4][i-1] ==  'Name' and list_final[4][i-2] == 'Block':
        flag_block = 1
    if list_final[4][i] == 'School':
        flag_block = 0
    if flag_block == 1:
        Block_Name += list_final[4][i] + ' '
    if list_final[4][i-1] == 'Name' and list_final[4][i-2] == '&' and list_final[4][i-3] == 'Code' and list_final[4][i-4] == 'School':
        flag_school_code = 1
    if flag_school_code == 1:
        School_code_Name += list_final[4][i] + ' '

flag_pin = 0
flag_headmaster = 0
for i in range(2,len(list_final[5])):
    if list_final[5][i-1] ==  'PINCODE':
        flag_pin = 1
    if list_final[5][i] == 'Name':
        flag_pin = 0
    if flag_pin == 1:
        PINCODE += list_final[5][i] + ' '
    if (list_final[5][i-1] == 'Master' or list_final[5][i-1] == 'Maste') and list_final[5][i-2] == 'Head' and list_final[5][i-3] == 'of' and list_final[5][i-4] == 'Name':
        flag_headmaster = 1
    if flag_headmaster == 1:
        Name_of_HeadMaster += list_final[5][i] + ' '

flag_management = 0
flag_school_cateogry = 0
flag_school_type = 0
for i in range(2,len(list_final[6])):
    if list_final[6][i-1] ==  'Management':
        flag_management = 1
    if list_final[6][i] == 'School' and list_final[6][i+1] == 'Category':
        flag_management = 0
    if flag_management == 1:
        Management += list_final[6][i] + ' '
    if (list_final[6][i-1] == 'Category') and list_final[6][i-2] == 'School':
        flag_school_cateogry = 1
    if list_final[6][i] == 'Type' and list_final[6][i+2] == 'School':
        flag_school_cateogry = 0
    if flag_school_cateogry == 1:
        School_Category += list_final[6][i] + ' '
    if list_final[6][i-1] == 'School' and list_final[6][i-3] == 'Type':
        flag_school_type = 1
    if flag_school_type == 1:
        School_Type += list_final[6][i] + ' '

flag_location = 0
flag_lowest_class = 0
flag_highest_class = 0
for i in range(2,len(list_final[8])):
    if list_final[8][i-1] ==  'Location':
        flag_location = 1
    if list_final[8][i] == 'Lowest' and list_final[8][i+1] == 'Class':
        flag_location = 0
    if flag_location == 1:
        Location += list_final[8][i] + ' '
    if (list_final[8][i-1] == 'Class') and list_final[8][i-2] == 'Lowest':
        flag_lowest_class = 1
    if list_final[8][i] == 'Highest' and list_final[8][i+1] == 'Class':
        flag_lowest_class = 0
    if flag_lowest_class == 1:
        Lowest_Class += list_final[8][i] + ' '
    if list_final[8][i-1] == 'Class' and list_final[8][i-2] == 'Highest':
        flag_highest_class = 1
    if list_final[8][i] == 'Working':
        flag_highest_class = 0
    if flag_highest_class == 1:
        Highest_Class += list_final[8][i] + ' '

flag_year_estab = 0
flag_weather_road = 0
flag_shift_school = 0
for i in range(2,len(list_final[9])):
    if list_final[9][i-1] ==  'Establishment' and list_final[9][i-3] == 'Year':
        flag_year_estab = 1
    if list_final[9][i] == 'Approachable' and list_final[9][i+4] == 'road':
        flag_year_estab = 0
    if flag_year_estab == 1:
        Year_estab += list_final[9][i] + ' '
    if (list_final[9][i-1] == 'road') and list_final[9][i-5] == 'Approachable':
        flag_weather_road = 1
    if list_final[9][i] == 'Shift' and list_final[9][i+1] == 'School':
        flag_weather_road = 0
    if flag_weather_road == 1:
        Weather_road += list_final[9][i] + ' '
    if list_final[9][i-1] == 'School' and list_final[9][i-2] == 'Shift':
        flag_shift_school = 1
    if list_final[9][i] == 'Instructional':
        flag_shift_school = 0
    if flag_shift_school == 1:
        Shift_school += list_final[9][i] + ' '

flag_year_estab = 0
flag_weather_road = 0
flag_shift_school = 0
for i in range(2,len(list_final[9])):
    if list_final[9][i-1] ==  'Establishment' and list_final[9][i-3] == 'Year':
        flag_year_estab = 1
    if list_final[9][i] == 'Approachable' and list_final[9][i+4] == 'road':
        flag_year_estab = 0
    if flag_year_estab == 1:
        Year_estab += list_final[9][i] + ' '
    if (list_final[9][i-1] == 'road') and list_final[9][i-5] == 'Approachable':
        flag_weather_road = 1
    if list_final[9][i] == 'Shift' and list_final[9][i+1] == 'School':
        flag_weather_road = 0
    if flag_weather_road == 1:
        Weather_road += list_final[9][i] + ' '
    if list_final[9][i-1] == 'School' and list_final[9][i-2] == 'Shift':
        flag_shift_school = 1
    if list_final[9][i] == 'Instructional':
        flag_shift_school = 0
    if flag_shift_school == 1:
        Shift_school += list_final[9][i] + ' '
# print(list_final)
fout.write(State +';' + District_Name + ';' + Village_Name + ';' + Cluster_Name + ';' + Block_Name + ';' + School_code_Name + ';' + PINCODE + ';' + Name_of_HeadMaster + ';' + Management + ';' + School_Category + ';' + School_Type + ';' + Location + ';' + Lowest_Class + ';' + Highest_Class + ';' + Year_estab + ';' + Weather_road + ';' + Shift_school + '\n')

# r = csv.reader(open('final.csv')) # Here your csv file
# lines = list(r)

fout.close()
# writer = csv.writer(open('final.csv', 'w'))
# writer.writerows(lines)
# a = zip(*csv.reader(open("basic_details.csv", "rb")))
# csv.writer(open("basic_details_transposed.csv", "wb")).writerows(a)