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
