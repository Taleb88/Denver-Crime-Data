import pandas as pd
import time

crime_df = pd.read_csv('csv/crime.csv', encoding='ISO-8859-1')
offense_codes_df = pd.read_csv('csv/offense_codes.csv', encoding='ISO-8859-1')

start_time = time.time()

print('\nread csvs - ', time.time() - start_time,'\n')

my_list = list(crime_df)
index = 0
for col_name in my_list:
    try: 
        print(index, col_name)
        index += 1
    except Exception as e:
        print(f'{type(e)}')
print('\ndisplay columns of crime.csv - ', time.time() - start_time, '\n')    

my_list = list(offense_codes_df)
index = 0
for col_name in my_list:
    try:         
        print(index, col_name)
        index += 1
    except Exception as e:
        print(f'{type(e)}')    
print('\ndisplay columns of offense_codes.csv - ', time.time() - start_time, '\n')
# print crime_df rows
print(crime_df)

# convert column names to lowercase format in offense_codes.csv
offense_codes_df.columns = map(str.lower, offense_codes_df.columns)
print(offense_codes_df)

merged_df = pd.merge(crime_df, offense_codes_df, on='offense_code')
print(merged_df.sort_values(by='offense_type_name', ascending=True).head(30))

offense_code_pivot_table_df = pd.pivot_table(merged_df, 
                                             index='offense_type_name',
                                             values='offense_category_name',
                                             aggfunc='count')
print(offense_code_pivot_table_df)
offense_code_pivot_table_df.to_csv('offense_code_pivot_table.csv')

#victim_count of 1
victim_count_df = crime_df.loc[crime_df['victim_count'] == 1]
print(victim_count_df.sort_values(by='reported_date', ascending=True))
victim_count_df.to_csv('victim_count.csv', index=False)

#victim_count of at least 2 (multiple victims)
multiple_victim_count_df = crime_df.loc[crime_df['victim_count'] >= 2]
print(multiple_victim_count_df.sort_values(by='reported_date', ascending=True))
multiple_victim_count_df.to_csv('multiple_victim_count.csv', index=False)

#neighborhood pivot table
print(crime_df['neighborhood_id'].unique()) #grabbing unique values first
neighborhood_crime_stats_pivot_table_df = pd.pivot_table(crime_df,
                                             index='neighborhood_id',
                                             values='victim_count',
                                             aggfunc='count')
print('\n victim count per neighborhood', neighborhood_crime_stats_pivot_table_df)
neighborhood_crime_stats_pivot_table_df.to_csv('neighborhood_crime_stats_pivot_table.csv')

# utilizing a groupby to display results of crimes per neighborhood in terms of type and total count per type
crime_description_per_neighborhood_df = crime_df.groupby(['neighborhood_id', 'offense_code', 'offense_type_id'])['victim_count'].sum()
print(crime_description_per_neighborhood_df)
crime_description_per_neighborhood_df.to_csv('crime_description_per_neighborhood.csv')
# top 5 most dangeerous neighborhoods in terms of crime rate
neighborhood_crime_stats_top_5_pivot_table_df = neighborhood_crime_stats_pivot_table_df.sort_values(by='victim_count', ascending=False).head(5)
print('\ntop 5 most dangerous neighborhoods: ',neighborhood_crime_stats_top_5_pivot_table_df)
neighborhood_crime_stats_top_5_pivot_table_df.to_csv('neighborhood_crime_stats_top_5_pivot_table.csv')

#charts
import matplotlib.pyplot as plt
import csv

open_file = open("neighborhood_crime_stats_top_5_pivot_table.csv","r")

csv_file = csv.reader(open_file)
next(csv_file, None)

neighorhood_id = []
victim_count = []

for row in csv_file:
    try: 
        neighorhood_id.append(row[0])
        victim_count.append(row[1])
    except Exception as e:
        print(f'{type(e)}')      

plt.pie(victim_count, labels=neighorhood_id, autopct='%1.0f%%')
plt.title('neighborhood crime stats - top 5 worst neighborhoods', fontsize=11, weight='bold') #2018-2022
plt.axis('equal')
plt.show()