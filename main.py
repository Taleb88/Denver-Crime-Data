import pandas as pd
import time

crime_df = pd.read_csv('csv/crime.csv', encoding='ISO-8859-1')
offense_codes_df = pd.read_csv('csv/offense_codes.csv', encoding='ISO-8859-1')

start_time = time.time()

print('\nread csvs - ', time.time() - start_time,'\n')

my_list = list(crime_df)
index = 0

for col_name in my_list:
    print(index, col_name)
    index += 1

print('\ndisplay columns of crime.csv - ', time.time() - start_time, '\n')    

my_list = list(offense_codes_df)
index = 0

for col_name in my_list:
    print(index, col_name)
    index += 1

print('\ndisplay columns of offense_codes.csv - ', time.time() - start_time, '\n')

# print crime_df rows
print(crime_df)

# column names to be in lowercase in offense_codes.csv
offense_codes_df.columns = map(str.lower, offense_codes_df.columns)
# print offense_codes_df rows
print(offense_codes_df)

print('\ncolumn names now in lowercase in offense_codes.csv - ', time.time() - start_time, '\n')